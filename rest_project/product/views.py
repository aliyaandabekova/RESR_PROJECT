from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class CategoryView(APIView):
     def get(self,request):
         category = Category.objects.all()
         serializer = CategorySerializer(category,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)

class CategoryProductsView(APIView):
    def get(self,request,*args,**kwargs):
        category = Category.objects.get(title=kwargs['cat_title'])
        products_all = category.product_set.all()
        serializer = ProductSerializer(products_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




