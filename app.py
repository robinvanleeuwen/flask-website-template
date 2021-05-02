import os

from flask_login import LoginManager
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logger import CustomLogger

log = CustomLogger()

login_manager = LoginManager()

base_dir = os.getcwd()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
