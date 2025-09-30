from rest_framework.views import APIView
from rest_framework.response import Response
from faker import Faker
import random

class FakerUserView(APIView):
    def get(self, request):
        fake = Faker()
        status_choices = ['active', 'inactive', 'invited', 'suspended']
        role_choices = ['superadmin', 'admin', 'cashier', 'manager']

        users = []
        jumlah_user = int(request.GET.get('jumlah', 10))  # bisa custom jumlah user lewat query param

        for _ in range(jumlah_user):
            user = {
                "id": fake.unique.random_int(min=1000, max=9999),
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "email": fake.email(),
                "status": random.choice(status_choices),
                "role": random.choice(role_choices),
                "createdAt": fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
            }
            users.append(user)

        return Response(users)