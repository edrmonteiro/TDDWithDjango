from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn ('<title>To-Do Lists</title>', response.content.decode())
        self.assertTrue(response.content.decode().strip().endswith('</html>'),
        f'html did not end correctly. was: {response.content}')
        self.assertTemplateUsed(response, 'home.html')

    # def test_handles_post_requests(self):
    #     response = self.client.post('/')
    #     self.assertIn('a list item', response.content)