from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from core.models import City, User

from core.db import get_db
from rq.job import Job
from .worker import conn
from rq import Queue
import requests

bp = Blueprint("city", __name__, url_prefix="/cities")


def search_zip_code(user_id):
    zip_code = User.query.filter_by(id=user_id).first().zip_code
    r = requests.get(f"https://service.zipapi.us/zipcode/{zip_code}?X-API-KEY=8b834b3df72a04223d32ea5f80351d37&fields=geolocation,population")
    print(r.json())
    return r.json()


@bp.route("/task/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)
    print(job)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202