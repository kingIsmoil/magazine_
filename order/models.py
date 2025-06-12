from django.db import models
from Accounts_user.models import User
from category.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    adress = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"{self.user} and {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='OrderItem', on_delete=models.CASCADE)    
    product = models.ForeignKey(Product, related_name='orderitem', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.order} and {self.product}"
    
    