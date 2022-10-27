USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'minha-senha-secreta'