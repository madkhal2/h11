from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # الصفحة الرئيسية
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # تفاصيل المنتج
]
