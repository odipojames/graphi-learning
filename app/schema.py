import graphene
from graphene_django import DjangoObjectType
from .models import Player, Coach
class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
class Query(graphene.ObjectType):
    player = graphene.Field(PlayerType, id=graphene.Int())#to get spacific
    players = graphene.List(PlayerType)#to get all

    def resolve_player(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Player.objects.get(pk=id)

        return None

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()


#Coach api
class CoachType(DjangoObjectType):
    class Meta:
        model = Coach

class Query(graphene.ObjectType):
    coaches = graphene.List(CoachType)

    def resolve_coaches(self, info, **kwargs):
        return Coach.objects.all()



# Create Input Object Types
class PlayerInput(graphene.InputObjectType):
    name = graphene.String()
    country = graphene.String()
    club = graphene.String()


# Create mutations for actors
class CreatePlayer(graphene.Mutation):
    class Arguments:
        input = PlayerInput(required=True)

    ok = graphene.Boolean()
    player = graphene.Field(PlayerType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        player_instance = Player(name=input.name,country=input.country,club=input.club)
        player_instance.save()
        return CreatePlayer(ok=ok, player=player_instance)

class UpdatePlayer(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PlayerInput(required=True)

    ok = graphene.Boolean()
    player = graphene.Field(PlayerType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        player_instance = Player.objects.get(pk=id)
        if player_instance:
            ok = True
            player_instance.name = input.name
            player_instance.country = input.country
            player_instance.club = input.club
            player_instance.save()
            return UpdatePlayer(ok=ok, player=player_instance)
        return UpdatePlayer(ok=ok, player=None)

class Mutation(graphene.ObjectType):
    create_player = CreatePlayer.Field()
    update_player = UpdatePlayer.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
