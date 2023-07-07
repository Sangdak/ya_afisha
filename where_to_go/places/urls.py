from django.urls import path, re_path
from .views import *

app_name = 'places'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('places/<int:place_id>', place_card, name='place')
]
