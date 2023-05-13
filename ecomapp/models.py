from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorys(models.Model):
    c_name=models.CharField(max_length=255)
    def __str__(self):
        return self.c_name

class Products(models.Model):
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    price=models.IntegerField()
    image=models.ImageField(upload_to="image/",null=True)
    def __str__(self):
        return self.name

