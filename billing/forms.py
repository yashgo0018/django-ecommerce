from django import forms

from .models import BillingProfile


class AddressForm(forms.ModelForm):
    class Meta:
        model = BillingProfile
        fields = [
            'name',
            'email',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'pincode'
        ]
