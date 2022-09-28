from django.db.utils import IntegrityError
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BillingProfile
from .serializers import BillingProfileSerializer


class BillingProfileAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BillingProfileSerializer

    def get_queryset(self):
        self.request.POST.user = self.request.user
        return self.request.user.billingprofile_set.all()

    def create(self, request, *args, **kwargs):
        # Get The Request Data
        name = request.data.get('name')
        email = request.data.get('email')
        address_line_1 = request.data.get('address_line_1')
        address_line_2 = request.data.get('address_line_2')
        city = request.data.get('city')
        state = request.data.get('state')
        country = request.data.get('country')
        pincode = request.data.get('pincode')
        # Make the user's profile and if any required field is empty then return error with status 400
        try:
            profile = self.request.user.billingprofile_set.create(
                name=name,
                email=email,
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                state=state,
                country_code=country,
                pincode=pincode
            )
        except IntegrityError as err:
            return Response({"error": "Insufficient Data"}, status=400)
        # If Everything goes smooth then return the profile
        return Response(self.serializer_class(profile).data)


class CountriesData(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        return Response(BillingProfile.CountriesChoises.choices)
