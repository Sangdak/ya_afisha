from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def show_start_page(request):
    places = Place.objects.all()

    context = {
        'places': {
            'type': 'FeatureCollection',
            'features': [],
        }
    }

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    place.lng,
                    place.lat
                ]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('places:place', args=[place.id])
            }
        }

        context['places']['features'].append(feature)

    return render(request, 'index.html', context)


def show_place_card(request, place_id):
    selected_place = get_object_or_404(Place, id=place_id)
    place_info = {
        'title': selected_place.title,
        'imgs': [img.image.url for img in selected_place.images.all()],
        'description_short': selected_place.description_short,
        'description_long': selected_place.description_long,
        'coordinates': {
            'lng': selected_place.lng,
            'lat': selected_place.lat
        }
    }
    return JsonResponse(
        place_info,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4,
        },
    )
