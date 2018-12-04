import os
from unittest import mock
from tempfile import mkdtemp
import flask_testing
from flask import url_for

from immutableweb import stream
from immutableweb import crypto
from immutablewebserver import app


class ServerTestCase(flask_testing.TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app


class IndexViewsTestCase(ServerTestCase):

    def setUp(self):
        self.dir = mkdtemp()
        app.config['STREAM_DIR'] = self.dir
        ServerTestCase.setUp(self)

        s = stream.Stream()
        self.public_key, self.private_key = crypto.make_key_pair()
        s.set_stream_signature_keys(self.public_key, self.private_key)
        self.uuid = s.uuid
        s.create(os.path.join(self.dir, "%s.iw" % self.uuid))
        s.append(b"1")
        s.append(b"2")
        s.append(b"3")
        s.close()


    def tearDown(self):
        try:
            os.unlink(self.dir)
        except IOError:
            pass


    def test_index(self):
        resp = self.client.get(url_for('index'))
        self.assert200(resp)


    def test_get(self):
        resp = self.client.get(url_for('uuid_get', id=self.uuid, block=1))
        self.assert200(resp)

        metadata, block = resp.data.split(b"\n")
        self.assertEqual(block, b"1")
