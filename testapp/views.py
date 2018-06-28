from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    context = {
            'test': 'this is a test'
            }
    return render(request, 'testapp/index.html', context)
