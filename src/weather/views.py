from os import name
from django.shortcuts import redirect, render
from decouple import config
import requests
from pprint import pprint
from .models import City
from .forms import CityForm
from django.contrib import messages

def index(request):
    form = CityForm()
    cities= City.objects.all()
    url = config('BASE_URL')
    # city = "Berlin"
    # respon = requests.get(url.format(city))
    # res = respon.json()
    # pprint(res)
    # print(type(res))
    # print(respon.text)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"] # => request.POST.get("name")
           
            if not City.objects.filter(name=new_city).exists():
                respon = requests.get(url.format(new_city))
                if respon.status_code == 200:
                    form.save()
                    messages.success(request, "City is added successfully!")
                else:
                    messages.warning(request, "City does not exist!!")
            else:
                messages.warning(request, "City is already exist!!")
            return redirect("weather:home")
    city_data = []
    for city in cities:
        respon = requests.get(url.format(city))
        res = respon.json()
        weather_data = {
            "city": city.name,
            "temp":res["main"]["temp"],
            "description":res["weather"][0]["description"],
            "icon":res["weather"][0]["icon"],
            
        }
        city_data.append(weather_data)
        
    context = {
        "city_data":city_data,
        "form":form
    }
    return render(request, "weather/index.html", context)
