from flask_testing import TestCase
from flask import current_app, url_for
import pytest

from app import app

from zip_code_app.db import get_db

class FactoryTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_index(self):
        response = self.client.get(url_for('index'))
        assert response.data == b"This is the app for the test"
