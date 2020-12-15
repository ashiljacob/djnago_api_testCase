
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer


class PostCustomerTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.customer =Customer.objects.create(
            name= "john",
            address = "address",
            phoneNumber = "2645662",
            gstin = "26456",
            outstandingbalance = 2356.26
        )

    def test_post(self):
        data = {
            "name": "john",
            "address": "address",
            "phoneNumber": "2645662",
            "gstin": "26456",
            "outstandingbalance": 2356.26 }
        
        response = self.client.post("/api/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get(self):
        response = self.client.get('/api',{},True)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_put(self):
        data = {
            "name": "test",
            "address": "address",
            "phoneNumber": "2645662",
            "gstin": "26456",
            "outstandingbalance": .36
            }

        response = self.client.put("/api/1/",data)
        serializer = CustomerSerializer(data)
        print(response.status_code)
        # self.assertEquals(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_delete(self):
        response = self.client.delete('api/1/')
        self.assertEquals(response.status_code,status.HTTP_204_NO_CONTENT)