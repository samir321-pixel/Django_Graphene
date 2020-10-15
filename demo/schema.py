import graphene
import graphene_app.schema
from graphene_django.debug import DjangoDebug
# from graphene_app.schema import Query
# from graphene_app.schema import Mutation

import graphene
#import django_graphql_movies.movies.schema
import graphene_app.schema


class Query(graphene_app.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(graphene_app.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
