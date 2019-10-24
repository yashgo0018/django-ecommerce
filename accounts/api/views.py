from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

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


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)
