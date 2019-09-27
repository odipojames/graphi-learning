from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home, name = 'home'),
    path(r'csv/',views.export,name= 'export'),
    path(r'json/',views.export_json,name= 'export_json'),
    path(r'exel/',views.export_exel,name= 'export_exel'),
    path(r'import/',views.import_dat,name= 'import_dat'),
    path(r'exportitem/',views.export_item,name= 'export_item'),
]
