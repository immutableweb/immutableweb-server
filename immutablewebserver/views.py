import os
import ujson
from flask import request, render_template
from werkzeug.exceptions import NotFound, BadRequest

from immutableweb import stream
from immutablewebserver import app


def validate_stream_id(id):
    if len(id) != 32:
        raise BadRequest("Invalid stream id.")
       
    try:
        _ = int(id, 16)
    except ValueError:
        raise BadRequest("Invalid stream id.")
        

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<id>/<int:block>')
def uuid_get(id, block):

    validate_stream_id(id)
    try:
        send_metadata = int(request.args.get('meta', '1'))
    except ValueError:
        raise BadRequest

    try:
        with stream.Stream(os.path.join(app.config["STREAM_DIR"], id + ".iw")) as s:
            metadata, block = s.read(block)

            if send_metadata:
                metadata = bytes(ujson.dumps(metadata), 'utf-8') + b"\n"
            else:
                metadata = bytes()

            return metadata + block

    except IOError:
        raise NotFound("No stream %s available." % id)
