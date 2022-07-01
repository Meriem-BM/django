from . import views
from django.urls import path

urlpatterns = [
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
    path('list/', views.PostList.as_view(), name='list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]