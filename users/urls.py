from django.urls import path
from .views import FakerUserBulkDeleteView, FakerUserView, FakerUserDetailView

urlpatterns = [
    path('faker-users/', FakerUserView.as_view(), name='faker-user-list'),
    path('faker-users/bulk-delete/', FakerUserBulkDeleteView.as_view(), name='faker-user-bulk-delete'),
    path('faker-users/<int:pk>/', FakerUserDetailView.as_view(), name='faker-user-detail'),
]