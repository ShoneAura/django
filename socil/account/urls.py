from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from account.views import ProfileView, RequestFriendsView, AcceptRequestFriendsView, FriendsView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:user_pk>/', ProfileView.as_view(), name='profile'),
    path('friends/requests/', RequestFriendsView.as_view(), name='request_friends'),
    path('friends/', FriendsView.as_view(), name='friends'),
    path('friends/requests/<int:user_pk>/', RequestFriendsView.as_view(), name='send_request_friends'),
    path('friends/requests/<int:user_pk>/<str:status>/', AcceptRequestFriendsView.as_view(), name='accept_request_friends'),
]
