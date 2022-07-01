from django.urls import path
from aboutme import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
]
