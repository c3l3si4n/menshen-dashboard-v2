from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {



    }
    return HttpResponse(template.render(context,request))


def target_detail(request, target_id):
    return HttpResponse('This is target %s.' % target_id)