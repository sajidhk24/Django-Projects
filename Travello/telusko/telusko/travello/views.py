from django.shortcuts import render
from .models import Destination

# Create your views here.


def travello(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'A city that never sleeps'
    dest1.price = 750
    dest1.img = 'destination_1.jpg'
    dest1.special_offer = True

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.description = 'City'
    dest2.price = 700
    dest2.img = 'destination_3.jpg'
    dest1.special_offer = False

    dest3 = Destination()
    dest3.name = 'Kolkata'
    dest3.description = 'City near hoogly river'
    dest3.price = 650
    dest3.img = 'destination_2.jpg'
    dest1.special_offer = True

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
