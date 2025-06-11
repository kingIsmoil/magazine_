from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    icon = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
class Subcategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title
    

class Product(models.Model):
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def str__(self):
        return self.title
    
class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return f"Image for {self.product_id.title}"
