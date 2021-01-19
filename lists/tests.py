from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    def test_math_works(self):
        response = self.client.get('/')
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn ('<title>To-Do Lists</title>', response.content.decode())
        self.assertTrue(response.content.decode().endswith('</html>'))