from django import forms
from django.urls import resolve
from django.conf import settings

symbol = settings.CURRENCY.symbol


class FilterForm(forms.Form):
    search = forms.CharField(label='Search', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control mr-sm-2',
        'placeholder': 'Search',
        'aria-label': 'Search',
    }))
    sort_by = forms.CharField(label='Sort By', widget=forms.Select(choices=[
        (0, 'Relavent'),
        (1, 'Sort By Price High To Low'),
        (2, 'Sort By Price Low To High')
    ], attrs={
        'class': 'form-control'
    }))
    max_price = forms.ChoiceField(label='Price', required=False, choices=[
        (50, f'Under {symbol}50'),
        (100, f'Under {symbol}100'),
        (200, f'Under {symbol}200'),
        (500, f'Under {symbol}500'),
        (1000, f'Under {symbol}1000')
    ], widget=forms.RadioSelect(attrs={
        'class': 'radio'
    }))
