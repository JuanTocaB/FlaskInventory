import requests
import os
from dotenv import load_dotenv


load_dotenv()

class ProductRepository:
    def __init__(self) -> None:
        self.products: list[dict] = requests.get(
            os.getenv("API_URL") + os.getenv("PRODUCTS_ENDPOINT")
        ).json()
    
    def get_all(self) -> list[dict]:
        """
        Get all products from the database.
        """
        return self.products