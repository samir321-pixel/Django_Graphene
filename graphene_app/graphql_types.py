from graphene import relay
import graphene
from graphene_django.types import DjangoObjectType
from .models import *
from graphene import Node
from graphene import Connection, Int
from django.contrib.auth.models import User, Group
from django_graphene_permissions import PermissionDjangoObjectType
from django_graphene_permissions.permissions import IsAuthenticated

#Activity GraphQL
class TaskType(DjangoObjectType):
    class Meta:
        model=task
        filter_fields='__all__'
        interfaces=(relay.Node,)