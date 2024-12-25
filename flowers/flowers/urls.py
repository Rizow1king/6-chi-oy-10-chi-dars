from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type/<int:type_id>/', category, name='type_detail'),
    path('type/<int:type_id>/update', update_species, name='update_species'),
    path('type/<int:type_id>/delete', delete_type, name='delete_type'),
    path('flower/<int:flower_id>/', flower, name='flower_detail'),
    path('flower/<int:flower_id>/update', update_flowers, name='update_flowers'),
    path('flower/<int:flower_id>/delete', delete_flowers, name='delete_flowers'),
    path('species/add/', add_species, name='add_species'),
    path('flowers/add/', add_flowers, name='add_flowers'),
]
