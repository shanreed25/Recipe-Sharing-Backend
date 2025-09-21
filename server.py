from flask import Flask, render_template
import pypyodbc as odbc
import requests


app = Flask(__name__)

#Sync Connection Variables
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'SHANNONHP\MSSQLSERVER01'
DATABASE_NAME = 'VeganRecipes'

#Specify the driver, server and database names
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
#connect function
conn = odbc.connect(connection_string)

# this cursor can be shared globally and reused across requests
# but closing it for each request will cause failures for subsequent requests
# it is better to create a new cursor per request instead 
# of the global one to avoid concurrency issues and unexpected errors
cursor = conn.cursor()#memory space

@app.route("/")# this function only triggers if the user is accessing the('/') route
def home():
    return render_template("index.html")

@app.route("/recipes")# this function only triggers if the user is accessing the('/recipes') route
def recipes():
    return render_template("recipes.html")

# a single dynamic route with a variable for the recipe type
@app.route("/recipes/type/<recipe_type>")# dynamic route with a variable for the recipe type
def get_recipes_by_type(recipe_type):
     # Mapping of recipe_type string to its corresponding ID
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
     # Query the database using the mapped ID
     recipe_type_id = recipe_type_map.get(recipe_type.lower())
     if recipe_type_id is None:
         return f"Unknown recipe type: {recipe_type}", 404
# creats a new cursor per request instead 
# of the global one to avoid concurrency issues and unexpected errors
     local_cursor = conn.cursor()
        # closing the cursor after use, is good practice
        # However, if an exception occurs during iteration, the cursor may not be closed
        # using a try...finally block or a context 
        # manager will ensure the cursor is always closed
     try:
            # Fetching all columns with SELECT * can be inefficient if the table has many columns 
            # or large data. Specify only the required columns (e.g., recipe_name, recipe_description) 
            # to reduce memory usage and improve performance.
         recipes_cursor = local_cursor.execute("SELECT recipe_name, recipe_description FROM recipes WHERE recipe_type_id = ?", [recipe_type_id])
         # print(recipes_cursor)
         recipes_list = []
         for row in recipes_cursor:
             recipe_name = row[0]
             recipe_description = row[1]
             recipes_list.append([recipe_name, recipe_description])
     finally:
         local_cursor.close()
     # Render the appropriate template and pass the recipes
    #  template_path = f"./recipe-categories/{recipe_type.lower()}.html"

    # a single file and dynamically passes in the recipe_type from the server to get a list for the selected category
     template_path = "recipe_category.html"
     return render_template(template_path, recipes=recipes_list, category_title=recipe_type)


# In pypyodbc, cursors should be closed after fetching data
# Closing the global cursor here will cause failures for subsequent database queries
# in other routes
# since the cursor is shared and reused the closing logic should be inside 
# each route after data fetching, or use a new cursor per request. 
# cursor.close()

if __name__ == "__main__":
    app.run(debug=True)

# The query result rows are accessed using row['recipe_name'], 
# but pypyodbc cursors by default return rows as tuples, not dictionaries
# This will raise a TypeError. You should either set the cursor to return dictionaries 
# or access columns by index, e.g., row[0].
    # recipe_name = row['recipe_name']
    # recipe_description = row['recipe_description']
    # recipe_name = row[0]
    # recipe_description = row[1]


# The query "SELECT * FROM recipes WHERE recipe_type_id = ?" uses positional parameters, 
# but the parameter is passed as a list [recipe_type_id]. pypyodbc expects either a 
# tuple or list, which is correct, but if recipe_type_id is None (when the mapping fails), 
# this will result in a query with a NULL parameter, which may not be intended. 
# The check on line 54 prevents this, but if the mapping ever returns 0, it will be 
# treated as falsy. Consider using if recipe_type_id is None: for clarity and correctness.
