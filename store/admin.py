from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, TestImage

# تسجيل النماذج بدون تخصيص
admin.site.register(Category)
admin.site.register(TestImage)  # ✅ نموذج اختبار Cloudinary

# تسجيل نموذج Product مع تخصيص عرض الصور
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60"/>', obj.image.url)
        return "No Image"

    image_tag.short_description = 'صورة'
