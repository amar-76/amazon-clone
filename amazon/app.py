from flask import Flask
from amazon import product
from amazon.settings import ProdConfig

print(__name__)
def create_app(config=ProdConfig):
    print('create_app()')
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)
    register_bluprints(app)
    return app


def register_bluprints(app):
    app.register_blueprint(product.views.blueprint, url_prefix='/products')
