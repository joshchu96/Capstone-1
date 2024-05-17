from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from api import search_name


app = Flask(__name__)
app.config['SECRET_KEY']='shhh'

toolbar = DebugToolbarExtension(app)

@app.route("/")
def homepage():
    """Homepage for drink app"""
    return render_template('home.html')

@app.route("/search", methods=["GET","POST"])
def search_cocktail():
    """Search for the drink by name"""
    search_input = request.form.get('search-form')
    data = search_name(search_input)
    if data['drinks'] != None:
        cocktail_list = [cocktail['strDrink'] for cocktail in data['drinks']]
        return render_template("display_cocktail.html", cocktail_list=cocktail_list)
    else:
        return render_template('error.html')


@app.route("/display_<cocktail_name>/info")
def cocktail_details(cocktail_name):
    """Display detailed info on cocktail"""
    #grab the image url
    data = search_name(cocktail_name)
    drink = data['drinks'][0]
    image = drink.get('strDrinkThumb')
    #instructions
    instructions = drink.get('strInstructions')
    #ingredients
    ingredients =[]
    for num in range(1,16):
        ingredient = drink.get(f'strIngredient{num}')
        measure = drink.get(f'strMeasure{num}')
        if ingredient:
            ingredients.append((ingredient,measure))

    return render_template('details_cocktail.html',cocktail_name=cocktail_name, image=image, instructions=instructions, ingredients=ingredients)
    


   

    
    