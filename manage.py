#!/usr/bin/env python3
import os
import sys

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from models import User

app.config.from_object(os.environ["APP_SETTINGS"])

migrate = Migrate(app=app, db=db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
