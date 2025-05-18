import os
import json
from dotenv import load_dotenv
from exceptions.productError import ProductError

load_dotenv()

class ProductRepository:
    def __init__(self) -> None:
        local_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../database/products.json")
        )
        with open(local_path, "r") as f:
            self.products = json.load(f)
    
    def get_all(self) -> list[dict]:
        return self.products
    
    def update_stock(self, product_id: int, change: int) -> dict:

        product_updated: dict = {}
        for product in self.products:
            if product["id"] == product_id:
                actual_stock:int = product["stock"]
                updated_stock:int = actual_stock + change
                if updated_stock < 0:
                    raise ProductError(
                        "Stock cannot be negative",
                        400
                    )
                product["stock"] = updated_stock
                product["disponible"] = product["stock"] > 0
                product_updated = product
                break
        if not product_updated:
            raise ProductError(
                "Product not found",
                404
            )
        return product_updated

