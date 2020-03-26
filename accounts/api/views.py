from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        try:
            user = User.objects.create_user(
                email=email, password=password, full_name=fullname, phone=phone)
            return Response(UserSerializer(user).data)
        except ValueError as err:
            return Response({'error': err}, status=400)
        except IntegrityError as err:
            return Response({'error': "User Already Exist"}, status=403)


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)
