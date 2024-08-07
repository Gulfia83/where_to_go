from django.shortcuts import render
from .models import Place

def index(request):
    places = Place.objects.all()

    places_json = {
        "type": "FeatureCollection",
            "features": []
            }
    
    for place in places:
        places_json["features"].append(
            {
                "type": "Feature",
                "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
                },
                "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": "static/places/moscow_legends.json"
                }
            },           
        )

    context = {'places': places_json}
    return render(request, 'index.html', context)
