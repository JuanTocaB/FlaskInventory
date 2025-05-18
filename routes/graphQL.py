from flask import Blueprint
from controllers.product import ProductController

graphqlRoutes: Blueprint = Blueprint(
    'graphql', 
    __name__,
    url_prefix='/graphql'
)

@graphqlRoutes.route('/', methods=['POST'])
def endpoint():
    return ProductController().graphql()