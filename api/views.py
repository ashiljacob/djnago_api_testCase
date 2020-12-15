from django.shortcuts import render

from rest_framework.views import APIView
from .models import Customer
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework import status
from django.http import Http404

class CustomerView(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self,request,format=None):
        cus = Customer.objects.all()
        serializer = CustomerSerializer(cus,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print("after Save")
            return Response({
                'Status':True,
                'Message':"Customer Added Successfully",
            },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
