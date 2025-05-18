import pytest
import graphene
from services.product import Query, Mutation, repository

# Build a schema for testing
schema = graphene.Schema(query=Query, mutation=Mutation)

# A simple dummy product class matching ProductType fields
class DummyProduct:
    def __init__(self, id, title, stock):
        self.id = id
        self.title = title
        self.stock = stock

def test_query_products_empty(monkeypatch):
    # Stub get_all to return empty list
    monkeypatch.setattr(repository, "get_all", lambda: [])
    query = """
    {
      products {
        id
        title
        stock
      }
    }
    """
    result = schema.execute(query)
    assert result.errors is None
    assert result.data == {"products": []}

def test_query_products_non_empty(monkeypatch):
    dummy = DummyProduct(id=1, title="Widget", stock=42)
    monkeypatch.setattr(repository, "get_all", lambda: [dummy])
    query = """
    {
      products {
        id
        title
        stock
      }
    }
    """
    result = schema.execute(query)
    print(result)
    assert result.errors is None
    assert result.data == {
        "products": [
            {"id": 1, "title": "Widget", "stock": 42}
        ]
    }

def test_update_stock_mutation(monkeypatch):
    updated = DummyProduct(id=2, title="Gadget", stock=100)
    def fake_update_stock(product_id, change):
        assert product_id == 2
        assert change == 10
        return updated
    monkeypatch.setattr(repository, "update_stock", fake_update_stock)

    mutation = """
    mutation {
      updateStock(productId: 2, change: 10) {
        product {
          id
          title
          stock
        }
      }
    }
    """
    result = schema.execute(mutation)
    assert result.errors is None
    assert result.data == {
        "updateStock": {
            "product": {"id": 2, "title": "Gadget", "stock": 100}
        }
    }