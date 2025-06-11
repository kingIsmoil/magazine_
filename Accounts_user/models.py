from django.db import models



class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    delivery_address = models.CharField(max_length=255)
    
    

class Delivery(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=255)
    
    
    
class Fawourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username} - {self.product}"
    
    
        