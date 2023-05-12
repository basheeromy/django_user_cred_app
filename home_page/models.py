from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100,default="sample")
    price = models.DecimalField(max_digits=7,decimal_places=2,default=1.00)
    rating = models.CharField(max_length=1)
    
    def __str__(self):
        return self.title