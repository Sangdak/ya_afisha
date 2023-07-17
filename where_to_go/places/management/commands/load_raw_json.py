from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Place, Image


def get_or_create_place(place_raw):
    place_entry, created = Place.objects.get_or_create(
        title=place_raw['title'],
        defaults={
            'description_short': place_raw.get('description_short', ''),
            'description_long': place_raw.get('description_long', ''),
            'coordinates_lng': place_raw.get('coordinates', {}).get('lng'),
            'coordinates_lat': place_raw.get('coordinates', {}).get('lat'),
        }
    )

    if created and place_raw['imgs']:
        # images = []
        for order_num, image_url in enumerate(place_raw.get('imgs'), start=1):
            response = requests.get(image_url)
            response_image = response.content
            image_file = ContentFile(response_image)

            images_entry = Image.objects.create(place=place_entry, order=order_num)
            images_entry.image.save(f'{order_num}.jpg', image_file, save=True)


class Command(BaseCommand):
    help = 'Load new place data from remote *.json file.'

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        place = response.json()

        get_or_create_place(place)

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help='Link to download file.'
        )
