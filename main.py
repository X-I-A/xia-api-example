import os
from flask import Flask, Blueprint, render_template
from xia_api_flask import Restful


app = Flask(__name__)
app.config.from_object("config." + os.environ.get("XIA_ENV", "prod").title() + "Config")

home = Blueprint('home',  __name__)


@home.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


api_blueprint = Restful.get_api_blueprint("api_v1")
app.register_blueprint(home)
app.register_blueprint(api_blueprint, url_prefix="/api/v1")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # pragma: no cover
