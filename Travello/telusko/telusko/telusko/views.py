from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'addition.html', {'result': res})