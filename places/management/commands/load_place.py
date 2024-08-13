import os
from io import BytesIO

import requests
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            type=str,
            help='Ссылка на json-файл'
            )

    @staticmethod
    def upload_images(place, imgs_urls):
        for num, img_url in enumerate(imgs_urls):
            response = requests.get(img_url)
            response.raise_for_status
            image = BytesIO(response.content)
            image_name = os.path.basename(img_url)
            image_obj, created = place.images.get_or_create(
                place=place.id,
                order=num
            )
            image_obj.img.save(image_name, image, save=True)

    def handle(self, *args, **options):
        url = options['json_url']
        response = requests.get(url)
        response.raise_for_status
        response_json = response.json()
        place, created = Place.objects.get_or_create(
            title=response_json['title'],
            defaults={
                'short_description': response_json['description_short'],
                'long_description': response_json['description_long'],
                'lat': response_json['coordinates']['lat'],
                'lon': response_json['coordinates']['lng']
                }
        )

        self.upload_images(place, response_json['imgs'])
        self.stdout.write(self.style.SUCCESS('Data loaded'))
