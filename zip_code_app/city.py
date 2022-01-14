from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from zip_code_app.models import City
from sqlalchemy import func

from zip_code_app.db import get_db

bp = Blueprint("city", __name__, url_prefix="/cities")


@bp.route("/", methods=['GET'])
def get_cities_groupby():
    cities = []
    db = get_db()
    cities_groupby = City.query.with_entities(City.latitude, City.longitude, func.count(City.id)).group_by(City.latitude, City.longitude).all()

    for city in cities_groupby:
        cities.append({
            'latitude': city[0],
            'longitude': city[1],
            'count': city[2]
        })
    return {
        "data": cities
    }


@bp.route("/all", methods=['GET'])
def get_cities_all():
    cities = []
    db = get_db()

    for city in City.query.all():
        cities.append(city.serialize())
    return {
        "data": cities
    }