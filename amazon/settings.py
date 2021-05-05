import os
class Config(object):
    SECRET_KEY = os.environ.get('AMAZON_CLONE_SECRET', 'secret-key')
    # this directory
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


# always store sensitive info in env variable
class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('AMAZON_CLONE_DB_URI', 'postgresql://username:password@localhost:5432/databasename')

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'amz.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'