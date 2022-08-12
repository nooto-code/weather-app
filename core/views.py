from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    try:
        context = None
        if 'city' in request.POST:
            city = request.POST['city']
        else:
            city = 'dubai'
            
        appid = 'c6b66c97f9e2dc63cea06554d6e294b3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': appid,
            'units': 'metric'
        }
        req = requests.get(url=url, params=params)
        res = req.json()
        
        try:
            name = res['name']
            country = res['sys']['country']
            temp = res['main']['temp']
            temp_min = res['main']['temp_min']
            temp_max = res['main']['temp_max']
            humid = res['main']['humidity']
            status = res['weather'][0]['main']
            icon = res['weather'][0]['icon']
            wind = res['wind']['speed']
        except:
            return render(request, 'core/error.html')
        

        context = {
            'name': name,
            'country': country,
            'temp': temp,
            'temp_min': temp_min,
            'temp_max': temp_max,
            'humid': humid,
            'status': status,
            'icon': icon,
            'wind': wind,
        }

        return render(request, 'core/index.html', context)
    
    except:
        return render(request, 'core/error.html')