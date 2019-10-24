from django import forms
from django.urls import resolve


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
        (50, 'Under $50'),
        (100, 'Under $100'),
        (200, 'Under $200'),
        (500, 'Under $500'),
        (1000, 'Under $1000')
    ], widget=forms.RadioSelect(attrs={
        'class': 'radio'
    }))


# class PriceRangeForm(forms.Form):
#     pricerange = forms.ChoiceField(label='Price', choices=[('Under $5', 'Under $5'), ('Under $10', 'Under $10'), ('Under $20', 'Under $20'), ('Under $40', 'Under $40')], widget=forms.RadioSelect(attrs={
#         'class': 'radio'
#     }))


# class SearchForm(forms.Form):
#     search = forms.CharField(label='', widget=forms.TextInput(attrs={
#         'class': 'form-control mr-sm-2',
#         'placeholder': 'Search',
#         'aria-label': 'Search',
#     }))


#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         super().__init__(*args, **kwargs)


#     def get_submit_url(self):
#         namespace = resolve(self.request.path)
#         if namespace == 'products':

#             return self.request.path
