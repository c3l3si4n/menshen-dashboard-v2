from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from .models import Target

def index(request):
    return render(request, 'targets/index.html', {})

def detail(request, target_id):
    return HttpResponse("You're looking at target %s" % target_id)

