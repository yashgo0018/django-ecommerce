from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from billing.models import BillingProfile

from .serializers import BillingProfileSerializer
from rest_framework.generics import ListCreateAPIView


class BillingProfileAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BillingProfileSerializer

    def get_queryset(self):
        self.request.POST.user = self.request.user
        return self.request.user.billingprofile_set.all()

    def create(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address_line_1 = request.POST.get('address_line_1')
        address_line_2 = request.POST.get('address_line_2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')

        profile = self.request.user.billingprofile_set.create(name=name, email=email, address_line_1=address_line_1,
                                                              address_line_2=address_line_2, city=city, state=state, country=country, pincode=pincode)
        return Response(self.serializer_class(profile).data)
