from django.urls import path
from django.views.generic.base import TemplateView
from home import views

urlpatterns = [
    path('create/', views.createOrder, name="create"),
    path('tutorial/', views.list, name="tutorial"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
