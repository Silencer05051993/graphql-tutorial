import graphene


class User(graphene.ObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone_number = graphene.String()

    def resolve_name(self, args, context, info):
        return 'Entropy'
