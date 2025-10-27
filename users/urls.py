from django.urls import path
from .views import FakerUserView, FakerUserDetailView

urlpatterns = [
    path('faker-users/', FakerUserView.as_view(), name='faker-user-list'),
    path('faker-users/<int:pk>/', FakerUserDetailView.as_view(), name='faker-user-detail'),
]