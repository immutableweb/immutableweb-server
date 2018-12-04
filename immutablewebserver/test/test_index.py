import os
from unittest import mock
import flask_testing
from flask import url_for

from immutablewebserver import app


class ServerTestCase(flask_testing.TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app



class IndexViewsTestCase(ServerTestCase):

    def setUp(self):
        ServerTestCase.setUp(self)

    def test_index(self):
        resp = self.client.get(url_for('index'))
        self.assert200(resp)
