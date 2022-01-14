from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from core.models import City

from core.db import get_db
from rq.job import Job
from .worker import conn
from rq import Queue
import requests

bp = Blueprint("city", __name__, url_prefix="/cities")


@bp.route("/task/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)
    print(job)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202