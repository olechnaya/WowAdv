from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertisement

class IndexView(LoginRequiredMixin,ListView):
    model = Advertisement
    template_name = "theWow/index.html"

class AdvDetailView(DetailView):
    model = Advertisement
    template_name = "theWow/adv_detail.html"
    context_object_name = 'adv'