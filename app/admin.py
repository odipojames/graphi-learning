from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from. models import Player, Item

# Register your models here.
@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    list_display =(

    'name',
    'country',
    'club'
    )
    list_per_page = 10

admin.site.register(Item)   
