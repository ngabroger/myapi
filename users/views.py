from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from faker import Faker
from datetime import datetime
import random
import math

fake = Faker()
fake.seed_instance(12345)

INITIAL_TOTAL = 200
status_choices = ['active', 'inactive', 'invited', 'suspended']
role_choices = ['superadmin', 'admin', 'cashier', 'manager']

ALL_USERS = []
for i in range(INITIAL_TOTAL):
    ALL_USERS.append({
        "id": 1000 + i,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "password": fake.password(length=10),  # plain text for testing only
        "status": random.choice(status_choices),
        "role": random.choice(role_choices),
        "createdAt": fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
    })

def _get_next_id():
    if not ALL_USERS:
        return 1000
    return max(u["id"] for u in ALL_USERS) + 1

def _paginate_list(items, page, limit):
    total_items = len(items)
    total_pages = math.ceil(total_items / limit) if limit else 1
    if page < 1:
        page = 1
    start = (page - 1) * limit
    end = start + limit
    return {
        "data": items[start:end],
        "pagination": {
            "current_page": page,
            "per_page": limit,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_previous": page > 1,
            "next_page": page + 1 if page < total_pages else None,
            "previous_page": page - 1 if page > 1 else None
        }
    }

class FakerUserView(APIView):
    """
    GET: list users (with pagination)
    POST: create new user (expects JSON body)
    """
    def get(self, request):
        page = int(request.GET.get('page', 1) or 1)
        limit = int(request.GET.get('limit', 10) or 10)
        if limit < 1:
            limit = 10
        if limit > 100:
            limit = 100

        result = _paginate_list(ALL_USERS, page, limit)
        return Response(result)

    def post(self, request):
        data = request.data or {}
        required = ["firstName", "lastName", "email"]
        for f in required:
            if not data.get(f):
                return Response({"detail": f"{f} is required"}, status=status.HTTP_400_BAD_REQUEST)

        new_user = {
            "id": _get_next_id(),
            "firstName": data.get("firstName"),
            "lastName": data.get("lastName"),
            "email": data.get("email"),
            "phone": data.get("phone", ""),
            "password": data.get("password", fake.password(length=10)),
            "status": data.get("status", random.choice(status_choices)),
            "role": data.get("role", "admin"),
            "createdAt": datetime.utcnow().isoformat() + "Z",
        }
        ALL_USERS.append(new_user)
        return Response(new_user, status=status.HTTP_201_CREATED)

class FakerUserDetailView(APIView):
    """
    GET / PUT / PATCH / DELETE for single user
    """
    def _find(self, pk):
        for u in ALL_USERS:
            if u["id"] == pk:
                return u
        return None

    def get(self, request, pk):
        user = self._find(pk)
        if not user:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(user)

    def put(self, request, pk):
        user = self._find(pk)
        if not user:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data or {}
        required = ["firstName", "lastName", "email"]
        for f in required:
            if not data.get(f):
                return Response({"detail": f"{f} is required"}, status=status.HTTP_400_BAD_REQUEST)

        user.update({
            "firstName": data.get("firstName"),
            "lastName": data.get("lastName"),
            "email": data.get("email"),
            "phone": data.get("phone", ""),
            "password": data.get("password", user.get("password")),
            "status": data.get("status", user.get("status")),
            "role": data.get("role", user.get("role")),
        })
        return Response(user)

    def patch(self, request, pk):
        user = self._find(pk)
        if not user:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data or {}
        allowed = {"firstName","lastName","email","phone","password","status","role"}
        for k, v in data.items():
            if k in allowed:
                user[k] = v
        return Response(user)

    def delete(self, request, pk):
        user = self._find(pk)
        if not user:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        ALL_USERS.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)