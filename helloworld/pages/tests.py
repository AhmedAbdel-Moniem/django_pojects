from django.test import TestCase

# Create your tests here.

class simple_test(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)