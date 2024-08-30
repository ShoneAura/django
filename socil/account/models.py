from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_unregistered = models.DateTimeField(auto_now=True)


class RequestFriends(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    user_from = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="user_from")
    user_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="user_to")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('user_from', 'user_to')
