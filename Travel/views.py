from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = 'mumbai'
    # dest1.desc = 'the city that never sleeps'
    # dest1.img = 'static/e1.jpg'
    # dest1.price = 700
    # dest1.offer = True


    # dest2 = Destination()
    # dest2.name = 'Punjab'
    # dest2.desc = 'pink city'
    # dest2.img = 'static/e2.jpg'
    # dest2.price = 890
    # dest2.offer= True
 
    # dest3 = Destination()
    # dest3.name = 'kerala'
    # dest3.desc = 'gods own country'
    # dest3.img = 'static/e3.jpg'
    # dest3.price = 1000
    # dest3.offer= False

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()
    
    return render(request,"index.html",{'dests': dests} )