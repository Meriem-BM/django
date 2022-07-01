from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', LogoutView.as_view(), name="logout"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path('/', login_required(TemplateView.as_view(template_name='login.html'))),
]
