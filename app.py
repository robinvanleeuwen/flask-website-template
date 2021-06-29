import os
import sys

from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory, request
from flask_cors import CORS
from flask_login import LoginManager

from logger import CustomLogger

log = CustomLogger()

login_manager = LoginManager()

base_dir = os.getcwd()

app = Flask(__name__)

# load_dotenv()

try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except KeyError as e:
    print(f"\033[93mEnvironment variables ({str(e)}) not setup!\033[0m")
    sys.exit()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

log.warning("LoginManager is not setup!")
# login_manager.init_app(app)
# login_manager.login_view = 'stream'

log.warning("SQLAlchemy is not setup!")
# engine = create_engine(os.environ['DATABASE_URL'])
# session_factory = sessionmaker(bind=engine)
# db_session = flask_scoped_session(session_factory, app)


@app.route("/")
def index():
    return render_template("index.html")


log.warning("Sitemap.xml and robots.txt are not configured!")


@app.route("/robots.txt")
@app.route("/sitemap.xml")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
