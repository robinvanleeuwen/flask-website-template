import os

from flask_login import LoginManager
from flask import Flask, render_template
from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logger import RsLogger

log = RsLogger()

login_manager = LoginManager()

base_dir = os.getcwd()

app = Flask(__name__)
login_manager.init_app(app)
login_manager.login_view = 'stream'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(os.environ['DATABASE_URL'])
session_factory = sessionmaker(bind=engine)
db_session = flask_scoped_session(session_factory, app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
