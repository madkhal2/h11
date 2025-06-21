from django.contrib import admin
from .models import Category, Product, TestImage  # استيراد النماذج الثلاثة

# تسجيل النماذج في لوحة تحكم Django Admin
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(TestImage)  # ✅ نموذج اختبار Cloudinary
