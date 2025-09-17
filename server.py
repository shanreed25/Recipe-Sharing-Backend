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
print(conn)#print to see if the connection is successful

#Pull data

cursor = conn.cursor()#memory space
all_recipes = cursor.execute("SELECT * FROM recipes")# send SQL command to the execute function

@app.route("/appetizers")# this function only triggers if the user is accessing the('/appetizers') route
def get_all_appetizers():
    # Print all data pulled from appetizers query
    appetizers = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 1")
    appetizers_list = []
    for row in appetizers:
        appetizer_name = row['recipe_name']
        appetizer_description = row['recipe_description']
        appetizers_list.append([appetizer_name, appetizer_description])
    print(appetizers_list)#print recipe name from each row
    return render_template("appetizers.html", appetizer_recipes=appetizers_list)


@app.route("/snacks")# this function only triggers if the user is accessing the('/snacks') route
def get_all_snacks():
    # Print all data pulled from snacks query
    snacks = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 8")
    snacks_list = []
    for row in snacks:
        snack_name = row['recipe_name']
        snack_description = row['recipe_description']
        snacks_list.append([snack_name, snack_description])
    print(snacks_list)#print recipe name from each row
    return render_template("snacks.html", snack_recipes=snacks_list)

@app.route("/breakfast")# this function only triggers if the user is accessing the('/breakfast') route
def get_all_breakfast():
    # Print all data pulled from breakfast query
    breakfast = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 2")
    breakfast_list = []
    for row in breakfast:
        breakfast_name = row['recipe_name']
        breakfast_description = row['recipe_description']
        breakfast_list.append([breakfast_name, breakfast_description])
    print(breakfast_list)#print recipe name from each row
    return render_template("breakfast.html", breakfast_recipes=breakfast_list)


@app.route("/brunch")# this function only triggers if the user is accessing the('/brunch') route
def get_all_brunch():
    # Print all data pulled from brunch query
    brunch = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 9")
    brunch_list = []
    for row in brunch:
        brunch_name = row['recipe_name']
        brunch_description = row['recipe_description']
        brunch_list.append([brunch_name, brunch_description])
    print(brunch_list)#print recipe name from each row
    return render_template("brunch.html", brunch_recipes=brunch_list)


@app.route("/soups")# this function only triggers if the user is accessing the('/soups') route
def get_all_soups():
    # Print all data pulled from soups query
    soups = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 3")
    soups_list = []
    for row in soups:
        soups_name = row['recipe_name']
        soups_description = row['recipe_description']
        soups_list.append([soups_name, soups_description])
    print(soups_list)#print recipe name from each row
    return render_template("soups.html", soups_recipes=soups_list)

@app.route("/stews")# this function only triggers if the user is accessing the('/stews') route
def get_all_stews():
    # Print all data pulled from stews query
    stews = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 4")
    stews_list = []
    for row in stews:
        stews_name = row['recipe_name']
        stews_description = row['recipe_description']
        stews_list.append([stews_name, stews_description])
    print(stews_list)#print recipe name from each row
    return render_template("stews.html", stews_recipes=stews_list)


@app.route("/salads")# this function only triggers if the user is accessing the('/salads') route
def get_all_salads():
    # Print all data pulled from salads query
    salads = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 5")
    salads_list = []
    for row in salads:
        salads_name = row['recipe_name']
        salads_description = row['recipe_description']
        salads_list.append([salads_name, salads_description])
    print(salads_list)#print recipe name from each row
    return render_template("salads.html", salads_recipes=salads_list)

@app.route("/entrees")# this function only triggers if the user is accessing the('/entrees') route
def get_all_entrees():
    # Print all data pulled from appetizers query
    entrees = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 7")
    entrees_list = []
    for row in entrees:
        entree_name = row['recipe_name']
        entree_description = row['recipe_description']
        entrees_list.append([entree_name, entree_description])
    print(entrees_list)#print recipe name from each row
    return render_template("entrees.html", entree_recipes=entrees_list)


@app.route("/sides")# this function only triggers if the user is accessing the('/sides') route
def get_all_sides():
    # Print all data pulled from sides query
    sides = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 2")
    sides_list = []
    for row in sides:
        sides_name = row['recipe_name']
        sides_description = row['recipe_description']
        sides_list.append([sides_name, sides_description])
    print(sides_list)#print recipe name from each row
    return render_template("sides.html", sides_recipes=sides_list)

if __name__ == "__main__":
    app.run(debug=True)




# @app.route("/appetizers")# this function only triggers if the user is accessing the('/appetizers') route
# def get_all_appetizers():
#     # Print all data pulled from appetizers query
#     appetizers = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 1")
#     appetizers_list = []
#     for row in appetizers:
#         recipe_name = row['recipe_name']
#         appetizers_list.append(recipe_name)
#         print(row['recipe_name'])#print recipe name from each row
#     return "<br>".join(f"<p>{name}</p>" for name in appetizers_list) 


# @app.route("/breakfast")# this function only triggers if the user is accessing the('/breakfast') route
# def get_all_breakfast():
#     # Print all data pulled from breakfast query
#     breakfast = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 2")
#     appetizers_list = []
#     for row in breakfast:
#         recipe_name = row['recipe_name']
#         appetizers_list.append(recipe_name)
#         print(row['recipe_name'])#print recipe name from each row
#     return "<br>".join(f"<p>{name}</p>" for name in appetizers_list) 



# @app.route("/entrees")# this function only triggers if the user is accessing the('/entrees') route
# def get_all_entrees():
#     # Print all data pulled from entrees query
#     entrees = cursor.execute("SELECT * FROM recipes WHERE recipe_type_id = 7")
#     appetizers_list = []
#     for row in entrees:
#         recipe_name = row['recipe_name']
#         appetizers_list.append(recipe_name)
#         print(row['recipe_name'])#print recipe name from each row
#     return "<br>".join(f"<p>{name}</p>" for name in appetizers_list) 