from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from post.views import PostView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('detail/<int:post_pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]
