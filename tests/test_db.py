from flask_testing import TestCase
from flask import current_app
import pytest
from app import app
from zip_code_app.db import get_db


class DBTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_db(self):
        db = get_db()
        self.assertEqual(db, get_db())
