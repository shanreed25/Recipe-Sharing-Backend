from flask import Flask, render_template
import pypyodbc as odbc
import requests


app = Flask(__name__)

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'SHANNONHP\MSSQLSERVER01'
DATABASE_NAME = 'VeganRecipes'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)

# cursor = conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/recipes/type/<recipe_type>")
def get_recipes_by_type(recipe_type):
     recipe_type_map = {
         "appetizers": 1,
         "breakfast": 2,
         "soups": 3,
         "stews": 4,
         "salads": 5,
         "sides": 6,
         "entrees": 7,
         "snacks": 8,
         "brunch": 9,
         "desserts": 10
     }

     recipe_type_id = recipe_type_map.get(recipe_type.lower())
     if recipe_type_id is None:
         return f"Unknown recipe type: {recipe_type}", 404

     local_cursor = conn.cursor()
     try:
         recipes_cursor = local_cursor.execute("SELECT recipe_name, recipe_description FROM recipes WHERE recipe_type_id = ?", [recipe_type_id])
         recipes_list = []
         for row in recipes_cursor:
             recipe_name = row[0]
             recipe_description = row[1]
             recipes_list.append([recipe_name, recipe_description])
     finally:
         local_cursor.close()

     template_path = "recipe_category.html"
     return render_template(template_path, recipes=recipes_list, category_title=recipe_type)

if __name__ == "__main__":
    app.run(debug=True)
