from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from zip_code_app.models import City

from zip_code_app.db import get_db

bp = Blueprint("city", __name__, url_prefix="/cities")


@bp.route("/", methods=['GET'])
def get_cities():
    cities = []
    for city in City.query.all():
        cities.append(city.serialize())
    print(cities)
    return {
        "data": cities
    }