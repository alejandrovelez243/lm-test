from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from core.models import User, City
from core.forms import UserForm
from core import q
from core.city import search_zip_code
from core.db import get_db

bp = Blueprint("client", __name__, url_prefix="/clients")

@bp.route("/", methods=("GET", "POST"))
def register():
    """Register a new client.
    """
    user_form = UserForm()
    if user_form.validate_on_submit():
        user_exist = User.query.filter_by(email=user_form.email.data).first()
        if not user_exist:
            db = get_db()
            user = User(
                first_name=user_form.first_name.data,
                last_name=user_form.last_name.data,
                middle_name=user_form.middle_name.data,
                zip_code=user_form.zip_code.data,
                email=user_form.email.data    
            )
            db.session.add(user)
            db.session.commit()
            job = q.enqueue_call(
                func=search_zip_code, args=(user.id,), result_ttl=5000
            )
            print(job.get_id())
            # Success, go to the client page.
            return redirect(url_for("client.client_json", user_id=user.id))
        flash('Email already registered')
    context = {
        'form': user_form
    }
    return render_template("client/register.html", **context)


@bp.route("/<user_id>")
def client_json(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user.serialize()
