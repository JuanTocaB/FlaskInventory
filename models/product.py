import graphene
from models.rating import RatingType

class ProductType(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    price = graphene.Float()
    description = graphene.String()
    category = graphene.String()
    image = graphene.String()
    rating = graphene.Field(RatingType)
    stock = graphene.Int()
    disponible = graphene.Boolean()