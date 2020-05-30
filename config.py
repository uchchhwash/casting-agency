import os
# basedir = os.path.abspath(os.path.dirname(__file__))
database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = project_dir + "\\app\\"
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

class Config(object):
    """Add configuration variables."""
    SQLALCHEMY_DATABASE_URI = database_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False