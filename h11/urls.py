from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ⬅ دعم static و media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),           # التطبيق الرئيسي
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# ✅ دعم static و media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
