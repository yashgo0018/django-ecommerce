from django.shortcuts import render
from django.views.generic import FormView
from .forms import AddressForm


class BillingProfileAddForm(FormView):
    template_name = 'contact.html'
    form_class = AddressForm

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)
