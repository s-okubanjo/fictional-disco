from django.test import TestCase
import json

# Create your tests here.


class ApiTest(TestCase):
    databases = {}

    def test_endpoint_returns_valid_content(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertTrue('data' in content)
        self.assertTrue('total' in content)
