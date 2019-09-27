from import_export import resources
from .models import Player, Item


class PlayerResource(resources.ModelResource):
    class Meta:
        model = Player
        # exclude = ['id']

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
