from django.shortcuts import render
from locations.models.voivodeship import Voivodeship


def view_map(request):
    voivodeships = Voivodeship.objects.all()
    return render(request, 'places/map.html', {'voivodeships': voivodeships})