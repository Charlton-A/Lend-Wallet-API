import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")


class DevelopmentConfig(Config):
    FLAAENV = "development"
    DEVELOPMENT = True
    TESTING = True
    SECRET_KEY = os.environ.get("APP_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("APP_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
