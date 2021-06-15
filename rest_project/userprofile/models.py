from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    wallet = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True,blank=True)
    order_count = models.PositiveIntegerField(default=0)
    sale = models.FloatField(default=0.0)
    def __str__(self):
        return self.full_name
