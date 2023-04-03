from django.urls import path
from. import views

urlpatterns = [
    path('<str:month>', views.monthly_challenges),
    path('', views.index, name='index')
]

