from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from userprofile.models import Profile
from product.models import Product,Category

class OrderPostTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaad',email='aliya@gmail.com',address='asdfg')
        self.category = Category.objects.create(title='laptop')
        self.product = Product.objects.create(name='jkl', category=self.category, desc='hjkl', price=56789)
        self.url = reverse('order')
