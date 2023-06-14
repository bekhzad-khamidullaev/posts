from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
]