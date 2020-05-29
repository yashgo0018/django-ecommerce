from rest_framework import serializers

from users.serializers import UserSerializer

from .models import BillingProfile


class BillingProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    country = serializers.SerializerMethodField()

    class Meta:
        model = BillingProfile
        fields = ['id', 'user', 'name', 'email', 'address_line_1',
                  'address_line_2', 'city', 'state', 'country_code', 'pincode', 'country']

    def get_country(self, obj):
        return obj.country
