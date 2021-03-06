import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    """Add configuration variables."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test_Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


TEST_MODE = os.environ.get('TEST_MODE')
