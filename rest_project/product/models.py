from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=100)
    price = models.FloatField(default=0.0)
    photo = models.ImageField(null=True,blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
