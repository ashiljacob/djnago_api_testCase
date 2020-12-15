
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
    
