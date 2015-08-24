from app import app
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY']='you-will-never-guess-hhh'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
