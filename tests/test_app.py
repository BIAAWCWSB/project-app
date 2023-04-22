import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World!", response.data)

    def test_hello(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)

    def test_hello_post(self):
        response = self.client.post('/hello', data=dict(name='John'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, John!", response.data)

if __name__ == '__main__':
    unittest.main()
