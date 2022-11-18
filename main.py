import os
from flask import Flask, Blueprint, render_template
from xia_api_flask import Restful, OpenApiPages


app = Flask(__name__)
app.config.from_object("config.Config")


api_blueprint = Restful.get_api_blueprint("api_v1")
api_doc_blueprint = OpenApiPages.get_api_doc_blueprint("api_doc")

app.register_blueprint(api_blueprint, url_prefix=app.config.get("API_PREFIX", "/api"))
app.register_blueprint(api_doc_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # pragma: no cover
