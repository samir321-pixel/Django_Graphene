import graphene
from .models import *
from .graphql_types import *
from graphql_relay import from_global_id
from graphene import relay
from graphql import GraphQLError


class TaskInput(graphene.InputObjectType):
    id = graphene.ID
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    date = graphene.types.datetime.DateTime(required=True)


class CreateTaskMutation(relay.ClientIDMutation):
    tsk = graphene.Field(TaskType, required=False)

    class Input:
        title = graphene.String()
        description = graphene.String()
        date = graphene.types.datetime.Date()

    @classmethod
    def mutate_and_get_payload(cls, root, info, title=None, description=None, date=None):
        login_user = info.context.user
        obj = {}
        obj = {
            "title": title,
            "description": description,
            "date": date,
        }
        q_1 = task.objects.create(user=login_user, **obj)
        return CreateTaskMutation(tsk=q_1)


class UpdateTaskMutation(relay.ClientIDMutation):
    tsk = graphene.Field(TaskType, required=False)

    class Input:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        date = graphene.types.datetime.Date()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id=None, title=None, description=None, date=None):
        login_user = info.context.user
        tsk_obj = task.objects.get(id=from_global_id(id)[1])

        if title:
            tsk_obj.title = title

        if description:
            tsk_obj.description = description

        if date:
            tsk_obj.date = date

        tsk_obj.save()

        return UpdateTaskMutation(tsk=tsk_obj)


class DeleteTaskMutation(relay.ClientIDMutation):
    tsk = graphene.Field(TaskType, required=False)

    class Input:
        id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id=None):

        if task.objects.filter(id=from_global_id(id)[1]).exists():
            # status = True
            msg = "Deleted"

            task.objects.filter(id=from_global_id(id)[1]).delete()
        else:
            # status=False
            msg = "Already Deleted or Dosent Exists"
            print("data dosent exits")
        return DeleteTaskMutation()


# class GetOneTaskMutation(relay.ClientIDMutation):
#     tsk = graphene.Field(TaskType, required=False)
#
#     class Input:
#         id = graphene.ID(required=True)
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, id=None):
#         login_user = info.context.user
#         tsk_obj = task.objects.get(id=from_global_id(id)[1])
#         tsk = task{
#             title = task.objects.get('title')
#         ,
#         }
#         if tsk_obj:
#             id = task.objects.values('id')
#             title = task.objects.values('title')
#             description = task.objects.values('description')
#             date = task.objects.values('date')
#             return GetOneTaskMutation(id, title, description, date)
