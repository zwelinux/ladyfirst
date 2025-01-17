from django.db import models

class Product(models.Model):
    seller = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=50)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    second_hand_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image_urls = models.JSONField()
    authenticity_docs = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('sold', 'Sold')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title