from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    places_details = {
        'type': 'FeatureCollection',
        'features': [{
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lon, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('place', kwargs={'place_id': place.pk})
                }
            } for place in places]
            }

    context = {'places': places_details}
    return render(request, 'index.html', context)


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }

    return JsonResponse(place_details,
                        json_dumps_params={'ensure_ascii': False, 'indent': 4})
