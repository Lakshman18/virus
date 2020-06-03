from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    url ='https://covid19.mathdro.id/api/'
    r = requests.get(url.format()).json()

    x = r['confirmed']['value']
    x1 = "{:,}".format(x)

    y = r['recovered']['value']
    y1 = "{:,}".format(y)

    z = r['deaths']['value']
    z1 = "{:,}".format(z)

    country_stats = {
            'confirmed' : x1,
            'recovered' : y1,
            'deaths' : z1,
            'update' : r['lastUpdate'][:10] ,
        }

    context = {"country_stats": country_stats}
    print(context)


    if request.method == 'POST':
        if request.POST['country'] == 'global':
            url ='https://covid19.mathdro.id/api/'
            r = requests.get(url.format()).json()

            x = r['confirmed']['value']
            x1 = "{:,}".format(x)

            y = r['recovered']['value']
            y1 = "{:,}".format(y)

            z = r['deaths']['value']
            z1 = "{:,}".format(z)

            country_stats = {
                    'confirmed' : x1,
                    'recovered' : y1,
                    'deaths' : z1,
                    'update' : r['lastUpdate'][:10] ,
                }

            context = {"country_stats": country_stats}
            print(context)

        else:
            c = request.POST['country']
            url ='https://covid19.mathdro.id/api/countries/{}'
            country = c

            r = requests.get(url.format(country)).json()

            x = r['confirmed']['value']
            x1 = "{:,}".format(x)

            y = r['recovered']['value']
            y1 = "{:,}".format(y)

            z = r['deaths']['value']
            z1 = "{:,}".format(z)

            country_stats = {
                    'confirmed' : x1,
                    'recovered' : y1,
                    'deaths' : z1,
                    'update' : r['lastUpdate'][:10] ,
                }

            context = {"country_stats": country_stats}
            print(context)

            return render(request, 'index.html',context)

    return render(request,'index.html', context)
