from django.shortcuts import render, get_object_or_404
from .models import Product

# عرض الصفحة الرئيسية مع قائمة المنتجات
def home_view(request):
    products = Product.objects.filter(available=True).order_by('-created_at')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

# عرض تفاصيل منتج واحد
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
