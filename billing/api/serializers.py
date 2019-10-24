from rest_framework import serializers
from billing.models import BillingProfile


class BillingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingProfile
        fields = ['id', 'user', 'name', 'email', 'address_line_1',
                  'address_line_2', 'city', 'state', 'country', 'pincode']
