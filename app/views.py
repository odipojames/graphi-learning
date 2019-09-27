from django.shortcuts import render
from django.http import HttpResponse
from .resources import  PlayerResource, ItemResource
from . models import Player
from tablib import  Dataset
# Create your views here.

def home(request):

    return HttpResponse('it must work in Jesus Name!')



def export(request):
    '''
    eport to csv file
    '''
    player_resource = PlayerResource()
    # queryset = Player.objects.filter(club='Chelsea')#for manupulation and pass queryset as agurment of expoert
    dataset = player_resource.export()
    response = HttpResponse(dataset.csv,content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="players.csv"'
    return response


def export_json(request):
    '''
    eport to jsons file
    '''
    player_resource = PlayerResource()
    # queryset = Player.objects.filter(club='Chelsea')#for manupulation and pass queryset as agurment of expoert
    dataset = player_resource.export()
    response = HttpResponse(dataset.csv,content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="players.json"'
    return response

def export_exel(request):
    '''
    eport to spreadsheet file
    '''
    player_resource = PlayerResource()
    # queryset = Player.objects.filter(club='Chelsea')#for manupulation and pass queryset as agurment of expoert
    dataset = player_resource.export()
    response = HttpResponse(dataset.csv,content_type='application/vnd.ms-exel')
    response['Content-Disposition'] = 'attachment; filename="players.xls"'
    return response


def export_item(request):
    '''
    export to spreadsheet file
    '''
    item_resource = ItemResource()
    # queryset = Player.objects.filter(club='Chelsea')#for manupulation and pass queryset as agurment of expoert
    dataset = item_resource.export()
    response = HttpResponse(dataset.csv,content_type='application/vnd.ms-exel')
    response['Content-Disposition'] = 'attachment; filename="items.xls"'
    return response


def import_dat(request):
    if request.method == 'POST':
        player_resource = PlayerResource()
        dataset = Dataset()
        new_players = request.FILES['myfile']

        imported_data = dataset.load(new_players.read())
        result = player_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            player_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import.html')
