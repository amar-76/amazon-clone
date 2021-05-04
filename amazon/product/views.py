
from flask import Blueprint, render_template
from .models import Product

blueprint = Blueprint('products', __name__, template_folder='templates') 

@blueprint.route('/')
def products():
    return render_template('products.html')
