import os
from flask import Flask
from xia_api_flask import Restful
from xia_engine_test import DocumentSimple


app = Flask(__name__)

api_blueprint = Restful.get_api_blueprint("api_v1")
app.register_blueprint(api_blueprint, url_prefix="/api/v1")
app.config["resource_mapping"] = {
    "Simple": DocumentSimple
}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # pragma: no cover
