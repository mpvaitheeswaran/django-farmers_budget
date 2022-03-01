from datetime import date
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Crop(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=15)
    total_expense = models.FloatField(default=0,blank=True)
    crop_value = models.FloatField(default=0,blank=True)
    date = models.DateTimeField(auto_now_add=False)
    is_closed = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.crop_name}'

class Expense(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    cost = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.name}'

class Market(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=25,blank=True)
    mass = models.FloatField(default=0)
    rate_per_kg = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)