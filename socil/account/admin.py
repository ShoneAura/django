from django.contrib import admin

from account.models import UserProfile, RequestFriends


class UserProfileAdin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'bio', 'date_registered')


class RequestFriendsAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'status')


admin.site.register(RequestFriends, RequestFriendsAdmin)
admin.site.register(UserProfile, UserProfileAdin)
