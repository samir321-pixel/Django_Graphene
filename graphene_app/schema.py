import graphene
from graphene import relay
from django_filters import FilterSet, OrderingFilter
import django_filters
from .graphql_types import *
from .mutations import *
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth.models import User
from graphene_django.filter import DjangoFilterConnectionField


class TaskFilter(FilterSet):
    class Meta:
        model = task
        fields = '__all__'


class Query(ObjectType):
    Task = relay.Node.Field(TaskType)
    # Activities API
    get_task = DjangoFilterConnectionField(TaskType, filterset_class=TaskFilter)
    # get_task_by_id=DjangoFilterConnectionField(TaskType,id=graphene.String())
    get_task_by_id = DjangoFilterConnectionField(TaskType, id=graphene.String(required=True))

    def resolve_activities(self, info, **kwargs):
        return task.objects.all()

    def resolve_activity(self, root, info, id):
        # id = kwargs.get('id')
        #
        # if id is not None:
        #     return task.objects.get(id=id)
        # sam=task.objects.filter(id=id)
        # if sam.exists():
        #     title=task.objects.get(title)
        #     description=task.objects.get(de)
        pass
        # return task.objects.get(id=id)


class Mutation(graphene.ObjectType):
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()
    delete_task = DeleteTaskMutation.Field()
    #get_onetask=GetOneTaskMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
