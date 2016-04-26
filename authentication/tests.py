from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import Account

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.

        """
        #This doesn't appear to be working. It can't find the right url.
        url = reverse(r'accounts')
        data = {'username': 'John.Doe', 'email':'John.Doe@nowhere.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().username, 'John.Doe')
