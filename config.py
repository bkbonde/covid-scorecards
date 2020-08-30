from os import environ, path

class Config:
    """Set Flask configuration from environment variables."""

    SERVER_NAME = environ.get('SERVER_NAME')
    #SERVER_PORT = environ.get('SERVER_PORT')
    # General Config
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get("SECRET_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Caching
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

    # Flask-Session
    SESSION_TYPE = 'filesystem'
