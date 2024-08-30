from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from account.models import UserProfile, RequestFriends


# Create your views here.


class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, user_pk):
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            return redirect('home')
        context = {
            "user": user,
            "my_profile": True if request.user == user else False
        }
        return render(request, self.template_name,  context=context)


class FriendsView(LoginRequiredMixin, View):
    template_name = 'friends.html'

    def get(self, request):
        friends = RequestFriends.objects.filter(Q(user_from=request.user) | Q(user_to=request.user))
        context = {
            "friends": friends,
        }
        return render(request, self.template_name,  context=context)


class RequestFriendsView(LoginRequiredMixin, View):
    template_name = 'request_friends.html'

    def get(self, request):
        request_users = RequestFriends.objects.filter(Q(user_to=request.user) & Q(status="pending"))
        context = {
            "request_users": request_users,
        }
        return render(request, self.template_name,  context=context)

    def post(self, request, user_pk):
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            return redirect('home')

        if RequestFriends.objects.filter(user_from=request.user, user_to=user).exists():
            return redirect('request_friends')

        RequestFriends.objects.create(user_from=request.user, user_to=user, status="pending")
        return redirect('request_friends')


class AcceptRequestFriendsView(LoginRequiredMixin, View):
    # template_name = 'request_friends.html'

    def post(self, request, user_pk, status):
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            return redirect('home')

        request_friend = RequestFriends.objects.get(user_from=user, user_to=request.user)
        request_friend.status = "accepted" if status == "accept" else "rejected"
        request_friend.save()
        return redirect('request_friends')
