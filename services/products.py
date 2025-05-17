from repositories.products import ProductRepository

class ProductService:
    def __init__(self) -> None:
        self.product_repository = ProductRepository()

    def get_all(self) -> list[dict]:
        """
        Get all products from the database.
        """
        return self.product_repository.get_all()