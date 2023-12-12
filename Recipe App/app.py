from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import unquote

app = Flask(__name__)

API_KEY = 'ee37fc7e6d8d41ebae326ce097142651'

@app.route('/home', methods=['GET'])
def home():
    home_query = ""
    recipes = search_recipes(home_query)
    return render_template('home.html', recipes=recipes, search_query=home_query)

@app.route('/submit', methods=['GET'])
def submit():
    submit_query = ""
    recipes = search_recipes(submit_query)
    return render_template('submit_recipe.html', recipes=recipes, search_query=submit_query)

@app.route('/about', methods=['GET'])
def about():
    about_query = ""
    recipes = search_recipes(about_query)
    return render_template('about_us.html', recipes=recipes, search_query=about_query)

@app.route('/meat', methods = ['GET'])
def meat():
    meat_query = "meat"
    recipes = search_recipes(meat_query)
    return render_template('home.html', recipes=recipes, search_query=meat_query)

@app.route('/seafood', methods=['GET'])
def seafood():
    seafood_query = "seafood"
    recipes = search_recipes(seafood_query)
    return render_template('home.html', recipes=recipes, search_query=seafood_query)

@app.route('/veggies', methods=['GET'])
def veggies():
    veggies_query = "vegetable"
    recipes = search_recipes(veggies_query)
    return render_template('home.html', recipes=recipes, search_query=veggies_query)

@app.route('/bevs', methods=['GET'])
def beverages():
    bevs_query = "beverage"
    recipes = search_recipes(bevs_query)
    return render_template('home.html', recipes=recipes, search_query=bevs_query)

@app.route('/breakfast', methods=['GET'])
def breakfast():
    breakfast_query = "breakfast"
    recipes = search_recipes(breakfast_query)
    return render_template('home.html', recipes=recipes, search_query=breakfast_query)

@app.route('/lunch', methods=['GET'])
def lunch():
    lunch_query = "lunch"
    recipes = search_recipes(lunch_query)
    return render_template('home.html', recipes=recipes, search_query=lunch_query)

@app.route('/dinner', methods=['GET'])
def dinner():
    dinner_query = "dinner"
    recipes = search_recipes(dinner_query)
    return render_template('home.html', recipes=recipes, search_query=dinner_query)

@app.route('/dessert', methods=['GET'])
def dessert():
    dessert_query = "dessert"
    recipes = search_recipes(dessert_query)
    return render_template('home.html', recipes=recipes, search_query=dessert_query)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If a form is submitted
        query = request.form.get('search_query', '')
        recipes = search_recipes(query)
        return render_template('home.html', recipes=recipes, search_query=query)
    
    # If it's a GET request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    recipes = search_recipes(decoded_search_query)
    return render_template('home.html', recipes=recipes, search_query=decoded_search_query)

# Function to search for recipes based on the provided query
def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 50,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    # Send a GET request to the Spoonacular API with the query parameters
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    return []

# Route to view a specific recipe with a given recipe ID
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    search_query = request.args.get('search_query', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }

    # Send a GET request to the Spoonacular API to get the recipe information
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True)
