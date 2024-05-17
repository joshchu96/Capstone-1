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
    cocktail_list = search_name(search_input)
    return render_template("display_cocktail.html", cocktail_list=cocktail_list)
