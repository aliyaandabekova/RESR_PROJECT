from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
from product.models import Category



class CommentTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaad')
        self.category = Category.objects.create(title='laptop')
        self.product = Product.objects.create(name='jkl',category=self.category,desc='hjkl',price=56789)
        self.url = reverse('product_detail',args=(self.product.id,))

    def test_comment_successful(self):
        self.client.login(username='aliya',password='123456')
        data = {
            'text':'good laptop'
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)

    def test_comment_with_bad_word(self):
        self.client.login(username='aliya',password='123456')
        data = {
            'text':'bad laptop'
        }
        self.response = self.client.post(self.url,data)
        self.assertContains(self.response,'bad boy',status_code=400)




class RateTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aliya', password='123456')
        self.profile = Profile.objects.create(user=self.user, full_name='aliyaad')
        self.category = Category.objects.create(title='laptop')
        self.product = Product.objects.create(name='jkl', category=self.category, desc='hjkl', price=56789)
        self.url = reverse('rate', args=(self.product.id,))
    def test_score_create(self):
        self.client.login(username='aliya',password='123456')
        data = {
            'score':5.0
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)


