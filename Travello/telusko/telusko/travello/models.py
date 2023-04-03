from django.db import models

# Create your models here.


class Destination:

    id = int
    name = str
    description = str
    img = str
    price = int
    special_offer = bool

