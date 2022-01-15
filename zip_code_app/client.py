from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from zip_code_app.models import User, City
from zip_code_app.forms import UserForm
from zip_code_app.db import get_db
import requests
from requests.auth import HTTPBasicAuth

bp = Blueprint("client", __name__, url_prefix="/clients")


def search_zip_code(zip_code):
    city = City.query.filter_by(zip_code=zip_code).first()
    if city:
        city_json = city.serialize_no_id()
        return city_json
    r = requests.get(f"https://service.zipapi.us/zipcode/{zip_code}?X-API-KEY=8b834b3df72a04223d32ea5f80351d37&fields=geolocation,county",
    auth=HTTPBasicAuth("alejandro-243@hotmail.com", "Ft1039469907"))
    if 'data' in r.json():
        return r.json().get("data")
    return None

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
            city = search_zip_code(user_form.zip_code.data)
            db.session.add(user)
            db.session.commit()
            if city:
                del city['county']
                city = City(**city, zip_code=user_form.zip_code.data)
                city.user = user
                db.session.add(city)
                db.session.commit()
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
