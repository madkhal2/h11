from django.shortcuts import render
from .models import Product  # تأكد أن موديل Product موجود في نفس التطبيق

def home_view(request):
    products = Product.objects.filter(available=True).order_by('-created_at')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)
