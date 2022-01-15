from flask_testing import TestCase
from flask import current_app, url_for
import pytest
from app import app
from city import CITY

class CityTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_get_all_cities(self):
        response = self.client.get(url_for('city.get_cities_all'))
        self.assert200(response)

    def test_group_by(self):
        response = self.client.get(url_for('city.get_cities_groupby'))
        self.assert200(response)
