from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

monthly = {
    'january': 'Walk for atleast 20 mins ',
    'feburary': 'Veg for a month ',
    'march': ' Learn Django ',
    'april': ' Learn something new ',
    'may': ' Eat no meat for entire month ',
    'june': 'Learn django for atleast 20 mins per day',
    'july': ' Learn some new language ',
    'august': ' Excise often',
    'september': 'Work on your projects',
    'october': 'Walk and workout for atleast an hour per hourd ',
    'november': '<h1>Help others</h1>',
    'december':  None  # '<h1>Use all of your senses and knowledge</h1>',
}


def index(request):
    month_list = list(monthly.keys())
    return HttpResponse(month_list)


def monthly_challenges(request, month):
    challenge_month = month
    challenge_text = monthly[month]
    return render(request, 'challenges.html', {
        "text": challenge_text,
        "month": challenge_month
    })


def index(request):
    month = list(monthly.keys())
    return render(request, "index.html", {
        "months": month
    })


