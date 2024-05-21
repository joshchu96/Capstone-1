import unittest
from app import app
from api import search_name

class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        

    def test_search_cocktail(self):
        response = search_name('Margarita')
        self.assertIn('drinks', response)
        drinks_list = [drink['strDrink'] for drink in response['drinks']]
        self.assertIn('Margarita', drinks_list) #check to see if margarita is inside the list of drinks.


    def test_search_cocktail_invalid(self):
        response = search_name('InvalidCocktailName')
        
        self.assertIn('drinks', response) 
        self.assertEqual(response['drinks'], None) 




