import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://qxozaxfyfougfj:ab0fbf8705456936ccf5fff735ef401df1aa771702c37ca3e8e04e68ad99443a@ec2-184-73-243-101.compute-1.amazonaws.com:5432/dbq8a4pquuv6j7"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost/testLM"

class TestingConfig(Config):
    TESTING = True