from flask_testing import TestCase
from flask import current_app, url_for
import pytest
from app import app
from zip_code_app.models import User
from zip_code_app.client import search_zip_code
from city import CITY
from client import CLIENT
import random
import string
import json

class ClientTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    @staticmethod
    def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    def test_register(self):
        response = self.client.get(url_for('client.register'))
        self.assert200(response)

        CLIENT['email'] = self.random_char(10)+"@hotmail.com"
        response = self.client.post(url_for('client.register'), data=CLIENT)
        self.assertStatus(response, 302)

        # test that the user was inserted into the database
        with app.app_context():
            self.assertIsNotNone(User.query.filter_by(email=CLIENT['email']).first())


    @pytest.mark.parametrize(
        ("username", "password", "message"),
        (
            ("", "", b"Username is required."),
            ("a", "", b"Password is required."),
            ("test", "test", b"already registered"),
        ),
    )
    def test_unique_email(self):
        CLIENT['email'] ="test@hotmail.com"
        response = self.client.post(
            url_for('client.register'), data=CLIENT
        )
        self.assertMessageFlashed('Email already registered')


    def test_user_id(self):
        CLIENT['email'] = self.random_char(10)+"@hotmail.com"
        response = self.client.post(url_for('client.register'), data=CLIENT)
        response = self.client.get(response.headers["Location"])
        self.assertEqual(CLIENT['email'], json.loads(response.get_data(as_text=True))['email'])

    def test_search_zip_code(self):
        result = search_zip_code("99501")
        self.assertIsNotNone(result)

    def test_search_zip_code_invalid(self):
        result = search_zip_code("JJJJ")
        self.assertIsNone(result)
