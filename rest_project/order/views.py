from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from .serializers import OrderSerializer

class OrderPostView(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        # profile = request.user.profile
        # product = Product.objects.get()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)