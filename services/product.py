import graphene
from models.product import ProductType
from repositories.product import ProductRepository

repository = ProductRepository()

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info):
        return repository.get_all()

class UpdateStock(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int(required=True)
        change = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, product_id, change):
        updated = repository.update_stock(product_id, change)
        return UpdateStock(product=updated)

class Mutation(graphene.ObjectType):
    update_stock = UpdateStock.Field()