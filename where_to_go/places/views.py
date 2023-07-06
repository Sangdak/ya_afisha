from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Image

from pprint import pprint


def start_page(request):
    # places = {
    #   "type": "FeatureCollection",
    #   "features": [
    #     {
    #       "type": "Feature",
    #       "geometry": {
    #         "type": "Point",
    #         "coordinates": [37.62, 55.793676]
    #       },
    #       "properties": {
    #         "title": "«Легенды Москвы",
    #         "placeId": "moscow_legends",
    #         "detailsUrl": "static/places/places/moscow_legends.json"
    #       }
    #     },
    #     {
    #       "type": "Feature",
    #       "geometry": {
    #         "type": "Point",
    #         "coordinates": [37.64, 55.753676]
    #       },
    #       "properties": {
    #         "title": "Крыши24.рф",
    #         "placeId": "roofs24",
    #         "detailsUrl": "static/places/places/roofs24.json"
    #       }
    #     }
    #   ]
    # }

    lst = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "static/places/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "static/places/places/roofs24.json"
            }
        },
    ]

    places = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in lst:
        places["features"].append(place)

    context = {
        'places': places,
    }

    pprint(places)

    return render(request, 'index.html', context)
