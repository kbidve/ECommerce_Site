from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", blank=True, null= True)
    image = models.ImageField(upload_to="uploads/products/")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_prod_by_catagory(catID):
        if catID:
            return Product.objects.filter(category = catID)
        else:
            return Product.objects.all()
