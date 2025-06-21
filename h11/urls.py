from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ⬅ هذا السطر يضيف دعم الملفات الثابتة

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),       # أو أي تطبيق رئيسي يعرض الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# ✅ هذا الجزء في نهاية الملف لتفعيل عرض الملفات الثابتة أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
