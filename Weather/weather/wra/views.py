from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    import json
    import requests

    if request.method == "POST":
        location = request.POST['location']
        # return render(request, 'wra/home.html', {'Location' : location})
        api_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + location + "&APPID=aae5c842e08a86ec6c65bd1bfab292aa")

    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api= "Error....."

    return render(request, 'wra/home.html', {'API': api})


def about(request):
    return render(request, 'wra/about.html', {'title': 'About'})


