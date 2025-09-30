from django.urls import path
from .views import FakerUserView, dashboard_view

urlpatterns = [
    path('faker-users/', FakerUserView.as_view(), name='faker-users'),
    path('dashboard/', dashboard_view, name='dashboard'),
]