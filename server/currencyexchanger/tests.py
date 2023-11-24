import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class CurrencyTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.response = json.loads('[]')

    def test_get(self):
        response = self.client.get('http://127.0.0.1:8000/currency/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), self.response)

