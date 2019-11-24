import graphene


class User(graphene.ObjectType):
    username = graphene.String()
    email = graphene.String()
