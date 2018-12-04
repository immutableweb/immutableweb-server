from flask import Flask


STATIC_PATH = "/static"
STATIC_FOLDER = "../static"
TEMPLATE_FOLDER = "../templates"

app = Flask(__name__,
    static_url_path = STATIC_PATH,
    static_folder = STATIC_FOLDER,
    template_folder = TEMPLATE_FOLDER)

import immutablewebserver.views
