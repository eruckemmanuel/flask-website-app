import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = bool(os.environ.get('DEBUG'))

# Application directory
BASE_DIR =  os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ.get('DB_USER'),
    os.environ.get('DB_PASSWORD'),
    os.environ.get('DB_HOST'),
    os.environ.get('DB_PORT'),
    os.environ.get('DB_NAME')
)
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2

# CSRF protection
CSRF_ENABLED = True

# Data signature
CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')

# Secret
SECRET_KEY = os.environ.get('SECRET_KEY')

