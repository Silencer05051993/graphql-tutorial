import graphene


class User(graphene.ObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone_number = graphene.String()

    def resolve_name(root, info):
        return 'Entropy'
    def resolve_email(root, info):
        return 'bac93.it@gmail.com'
