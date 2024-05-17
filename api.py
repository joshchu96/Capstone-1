from flask import jsonify
import requests

API_KEY=1
url = f"https://www.thecocktaildb.com/api/json/v1/{API_KEY}"
#since api key is stardard it will be included in the url variable

def search_name(cocktail_name):
    """Search for the cocktail by name"""
    cocktail_url = f"https://www.thecocktaildb.com/api/json/v1/{API_KEY}/search.php?s={cocktail_name}"
    response = requests.get(cocktail_url)

    #checks if request was successfull, 200
    if response.status_code == 200:
        data = response.json()
        drinks = data.get('drinks')
        if drinks:
            return data
        else: 
            return {'error': 'No drinks found with that name'}
    else:
        #if there is an error send a error message
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")
        return {'error': 'API request failed'}
    