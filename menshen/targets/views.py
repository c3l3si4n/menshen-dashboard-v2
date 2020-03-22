from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Target

class TargetList(ListView):
    model = Target

class TargetView(DetailView):
    model = Target

class TargetCreate(CreateView):
    model = Target
    fields = ['name']
    success_url = reverse_lazy('target_list')

class TargetUpdate(UpdateView):
    model = Target
    fields = ['name']
    success_url = reverse_lazy('target_list')

class TargetDelete(DeleteView):
    model = Target
    success_url = reverse_lazy('target_list')