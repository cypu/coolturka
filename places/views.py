from django.shortcuts import render


def view_map(request):
    return render(request, 'places/map.html')
