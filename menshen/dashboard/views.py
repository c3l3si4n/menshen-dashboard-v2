from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from targets.models import Target

def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {

        "target_count" : Target.objects.count()

    }
    return HttpResponse(template.render(context,request))
