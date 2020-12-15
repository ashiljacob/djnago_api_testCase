
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from .models import Customer
from .serializers import CustomerSerializer

# initialize the APIClient app
client = Client()

# Create your tests here.
class CustomerTest(TestCase):

    def setUp(self):
        Customer.objects.create(
            name='test',
            address = 'test',
            phoneNumber = '9586963',
            gstin = '25633',
            outstandingbalance = 2536.56
        )

    def test_customer_api(self):
    
        # get API response
        response = client.get(reverse('customer_get_post'))
        # get data from db
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class GetSinglePuppyTest(TestCase):
    """ Test module for GET single Customer API """

    def setUp(self):
        self.test = Customer.objects.create(
            name='test',
            address = 'test',
            phoneNumber = '9586963',
            gstin = '25633',
            outstandingbalance = 2536.56
        )
        

    def test_get_valid_single_customer(self):
        print("Testing ::::::::")

        response = client.get(
            reverse('customer_put_delete', kwargs={'pk': self.test.id}))

        customer = Customer.objects.get(id=self.test.id)
        print("Testing ::::::::",customer)

        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_customer(self):
        response = client.get(
            reverse('customer_put_delete', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)