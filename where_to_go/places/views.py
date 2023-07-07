from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def start_page(request):
    places = Place.objects.all()

    places_db = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.coordinates_lng,
                    place.coordinates_lat
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('places:place', args=[place.id])
            }
        }

        places_db["features"].append(feature)

    context = {'places': places_db}

    rend_page = render(request, 'index.html', context)

    return HttpResponse(rend_page)


def place_card(request, place_id):
    selected_place = get_object_or_404(Place, id=place_id)
    place_info = {
        'title': selected_place.title,
        'imgs': [img.get_url() for img in selected_place.images.all()],
        'description_short': selected_place.description_short,
        'description_long': selected_place.description_long,
        'coordinates': {
            'lng': selected_place.coordinates_lng,
            'lat': selected_place.coordinates_lat
        }
    }
    return JsonResponse(
        place_info,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4,
        },
    )
