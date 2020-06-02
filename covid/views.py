from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    url ='https://covid19.mathdro.id/api/'
    r = requests.get(url.format()).json()

    country_stats = {
            'confirmed' : r['confirmed']['value'],
            'recovered' : r['recovered']['value'],
            'deaths' : r['deaths']['value'],
            'update' : r['lastUpdate'][:10] ,
        }

    context = {"country_stats": country_stats}
    print(context)


    if request.method == 'POST':
        if request.POST['country'] == 'global':
            url ='https://covid19.mathdro.id/api/'
            r = requests.get(url.format()).json()

            country_stats = {
                'confirmed' : r['confirmed']['value'],
                'recovered' : r['recovered']['value'],
                'deaths' : r['deaths']['value'],
                'update' : r['lastUpdate'][:10] ,
            }

            context = {"country_stats": country_stats}
            print(context)
        
        else:
            c = request.POST['country']
            url ='https://covid19.mathdro.id/api/countries/{}'
            country = c

            r = requests.get(url.format(country)).json()

            country_stats = {
                'country' : c,
                'confirmed' : r['confirmed']['value'],
                'recovered' : r['recovered']['value'],
                'deaths' : r['deaths']['value'],
                'update' : r['lastUpdate'][:10] ,
            }

            context = {"country_stats": country_stats}
            print(context)

            return render(request, 'index.html',context)

    return render(request,'index.html', context)