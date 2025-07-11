from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='products/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ✅ نموذج اختبار لرفع الصور إلى Cloudinary
class TestImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='test_images/')

    def __str__(self):
        return self.title
