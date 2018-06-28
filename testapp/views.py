from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _ 


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    context = {
            'test': _('das ist ein test'),
            'variable': _('das ist eine variable')
            }
    return render(request, 'testapp/index.html', context)
