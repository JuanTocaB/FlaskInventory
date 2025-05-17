from flask import Blueprint
from controllers.products import ProductController

product_controller = ProductController()

apiRoutes: Blueprint = Blueprint(
    'api', 
    __name__,
    url_prefix='/api'
)

@apiRoutes.route('/hello')
def hello_world():
    return 'Hello, World!'

@apiRoutes.route('/products')
def products():
    return product_controller.index()