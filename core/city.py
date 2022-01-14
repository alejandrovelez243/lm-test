from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from core.models import City

from core.db import get_db
from rq.job import Job
from .worker import conn
from rq import Queue
import redis
import time

bp = Blueprint("city", __name__, url_prefix="/cities")

r = redis.Redis()
q = Queue(connection=r)


def search_zip_code(user_id):
    delay = 2
    print( " task running ")
    print(delay)
    time.sleep(delay)
    print("Task complete")
    return {"error": user_id}



@bp.route("/task", methods=['GET'])
def set_task():
    job = q.enqueue_call(search_zip_code, (1,))
    q_len = len(q)
    return f"Task {job.id} added to queue {q_len}"

@bp.route("/task/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)
    print(job)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202