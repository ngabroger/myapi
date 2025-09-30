from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from faker import Faker
import random
import math

class FakerUserView(APIView):
    def get(self, request):
        fake = Faker()
        status_choices = ['active', 'inactive', 'invited', 'suspended']
        role_choices = ['superadmin', 'admin', 'cashier', 'manager']

        # Pagination parameters
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        total_users = int(request.GET.get('total', 100))  # total data yang akan di-generate

        if page < 1:
            page = 1
        if limit < 1:
            limit = 10
        if limit > 100:  
            limit = 100

        # Hitung pagination
        total_pages = math.ceil(total_users / limit)
        start_index = (page - 1) * limit
        end_index = min(start_index + limit, total_users)

        users = []
        fake.seed_instance(12345)  

        all_users = []
        for i in range(total_users):
            user = {
                "id": 1000 + i,  # ID yang konsisten
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "email": fake.email(),
                "status": random.choice(status_choices),
                "role": random.choice(role_choices),
                "createdAt": fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
            }
            all_users.append(user)

        paginated_users = all_users[start_index:end_index]

        response_data = {
            "data": paginated_users,
            "pagination": {
                "current_page": page,
                "per_page": limit,
                "total_items": total_users,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_previous": page > 1,
                "next_page": page + 1 if page < total_pages else None,
                "previous_page": page - 1 if page > 1 else None
            }
        }

        return Response(response_data)


def dashboard_view(request):
    """View untuk menampilkan dashboard web dengan daftar users dan API endpoints"""
    return render(request, 'users/dashboard.html')