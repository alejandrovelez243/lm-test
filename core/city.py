from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from core.models import City

from core.db import get_db
from rq.job import Job

bp = Blueprint("city", __name__, url_prefix="/cities")


def search_zip_code(user_id):
    return {"error": user_id}


@bp.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202