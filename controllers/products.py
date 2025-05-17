from services.products import ProductService
from flask import jsonify
import json

class ProductController:

    def __init__ (self) -> None:
        self.product_service = ProductService()

    def index(self) -> json:
        products = self.product_service.get_all()
        return jsonify(products)