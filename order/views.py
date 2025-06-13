from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderListView(APIView):
    
    def get(self, request, id = None):
        if id:
            try:
                order = Order.objects.get(id = id)
                serializer = OrderSerializer(order)
                return Response({'order':serializer.data}, status=status.HTTP_200_OK)
            except Order.DoesNotExist:
                return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            orders = Order.objects.all()
            serializer = OrderItemSerializer(orders, many= True)
            return Response({'orders':serializer.data}, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, id = None):
        try:
            order = Order.objects.get(id = id)
        except Order.DoesNotExist:
            return Response({'message':'order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(order, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Order updated'}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id = None):
        try:
            order = Order.objects.get(id = id)
            order.delete()
            return Response({'message': 'Order deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

class OrderItemListView(APIView):
    
    def get(self, request, id = None):
        if id:
            try:
                oitem = OrderItem.objects.get(id = id)
                serializer = OrderItemSerializer(oitem)
                return Response({'oitem': serializer.data}, status=status.HTTP_200_OK)
            except OrderItem.DoesNotExist:
                return Response({'message': 'Orderitem not found'}, status=status.HTTP_404_NOT_FOUND)
               
        else:
            oitems = OrderItem.objects.all()
            serializer = OrderItemSerializer(oitems, many = True)
            return Response({'oitems': serializer.data}, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer = OrderItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, id = None):
        try:
            oitem = OrderItem.objects.get(id = id)
        except OrderItem.DoesNotExist:
            return Response({'message': 'Ordeitem not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderItemSerializer(oitem, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Orderitem updated'}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id = None):
        try:
            oitem = OrderItem.objects.get(id = id)
            oitem.delete()
            return Response({'message': 'Orderitem deleted'}, status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({'message': 'Orderitem not found'}, status=status.HTTP_404_NOT_FOUND)
               
         