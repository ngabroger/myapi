from django.urls import path
from .views import FakerUserView

urlpatterns = [
    path('faker-users/', FakerUserView.as_view(), name='faker-users'),
]