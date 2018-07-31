import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

passionpostgre = os.getenv('passionpostgre', None)

if passionpostgre is None:
    print('Specify passionpostgre as environment variable.')
    sys.exit(1)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = passionpostgre
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class slidepics(db.Model):
    __tablename__ = 'slidepics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    ext = db.Column(db.String(64))
    def __init__(self
                 , name
                 , ext
                 ):
        self.name = name
        self.ext = ext


class products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    picname = db.Column(db.String(256))
    picext = db.Column(db.String(64))
    external = db.Column(db.String(256))
    def __init__(self
                 , name
                 , picname
                 , picext
                 , external
                 ):
        self.name = name
        self.picname = picname
        self.picext = picext
        self.external = external

if __name__ == '__main__':
    manager.run()
