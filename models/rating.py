import graphene

class RatingType(graphene.ObjectType):
    rate = graphene.Float()
    count = graphene.Int()
