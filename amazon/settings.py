import os
class Config(object):
    SECRET_KEY = os.environ.get('AMAZON_CLONE_SECRET', 'secret-key')


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True