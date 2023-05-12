from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post

class IndexPageView(ListView):
    template_name = 'index.html'
    model = Post
class BlogPageView(ListView):
    template_name = 'blog.html'
    model = Post
class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Post

class AboutPageView(TemplateView):
    template_name = 'about.html'

# Create your views here.
