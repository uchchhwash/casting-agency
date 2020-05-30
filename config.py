import os
project_dir = os.path.abspath(os.path.dirname(__file__))
database_filename = "database.db"
#project_dir = project_dir + "\\app\\" #for windows
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

class Config(object):
    """Add configuration variables."""
    SQLALCHEMY_DATABASE_URI = database_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False