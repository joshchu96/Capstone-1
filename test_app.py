import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        

    def test_search_cocktail(self):
        response = self.app.post('/search', data={'search-form': 'Margarita'})
        print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, 200)
        

    def test_search_cocktail_invalid(self):
        response = self.app.post('/search', data={'search-form': 'InvalidCocktailName'})
        print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()

