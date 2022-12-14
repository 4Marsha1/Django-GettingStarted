from django.shortcuts import render, redirect
import json
import urllib.request

# Create your views here.
def index(request): 
    if request.method == "POST": 
        location = request.POST["location"]
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=873ef74993c289ed1864b583926cc8b1').read()
        json_data = json.loads(res)
        print(json_data)
        return redirect('/')
    else:
        location=""
        json_data={}
    return render(request, 'index.html', {'location':location, 'json_data': json_data})