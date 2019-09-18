import graphene
import app.schema
from app.schema import *

class Query(app.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)

schema = graphene.Schema(query=Query, mutation=Mutation)
