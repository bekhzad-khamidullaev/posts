from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post

class BasePageView(ListView):
    model = Post
    template_name = 'base.html'
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

# Create your views here.
