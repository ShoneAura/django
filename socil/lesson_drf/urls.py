
from django.urls import path

from lesson_drf.views import DRFView

urlpatterns = [
    path('', DRFView.as_view()),
]
