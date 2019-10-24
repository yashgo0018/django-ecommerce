from django.shortcuts import render, redirect
from order.models import Order

def user_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    model = Order.objects.all().filter(billing_profile__user = request.user).exclude(status='created')
    context={
        'model': model,
    }
    return render(request, 'user.html', context)
    
def user_security(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'user.html', {})
    
def user_address(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'user.html', {})