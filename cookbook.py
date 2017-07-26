#################################################
#                   RECIPES
#
# A small Flask app that handles my recipes and
# ingredients, and can generate shopping lists
#
# Written by Graham McCullough
#
#################################################

import os
import sqlite3
import datetime
import pymysql
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from sand import recipes, check_ingredients
#from flask.ext.mysql import MySQL

#mysql = MySQL()


#######
# create Flask app
#######
cookbook = Flask(__name__)

cookbook.config.update(dict(
    DEBUG=True
))

# MySQL config
def get_db():
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = pymysql.connect(
            host='localhost',
            user='recipes',
            password='WbGM6OMZ6QgVYrCM',
            db='Cookbook',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.mysql_db

@cookbook.teardown_appcontext
def close_db(error):
    # shut down the connection after the request
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

@cookbook.route('/')
def home():
    # link to new_recipe
    # link to ingredient_search
    # link to recipe_search
    return render_template('home.html')

@cookbook.route('/new_recipe', methods=['POST', 'GET'])
def new_recipe():
    # add a new recipe to the database
    # edit an existing recipe
    if request.method == 'POST':
        # update recipe, return view_recipe
        # create recipe, return view_recipe
        return view_recipe
    if request.method == 'GET':
        # return template form, filled out if update
        return render_template('new_recipe.html')

@cookbook.route('/view_recipe')
def view_recipe():
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute('select * from recipes where id="1";')
        recipe = cursor.fetchone()

    return render_template('view_recipe.html',
        name=recipe["name"],
        instructions=recipe["instructions"],
        prep_time=recipe["prep_time"],
        cook_time=recipe["cook_time"],
        num_servings=recipe["num_servings"],
        rating=recipe["rating"],
        times_made=recipe["times_made"],
        pic_ref=recipe["pic_ref"])

@cookbook.route('/test', methods=["POST", "GET"])
def test():
    msg = None
    allRecipes = recipes.keys()
    if request.method == "POST":
        myItems = request.form['ingredients'].split(', ')
        myRecipe = request.form['recipe']
        myRecipe_items = recipes[myRecipe]
        msg = check_ingredients(myItems, myRecipe_items)
        return render_template('test.html', message=msg, allrecipes=allRecipes)
    return render_template('test.html', message=msg, allrecipes=allRecipes)

if __name__ == "__main__":
    cookbook.run(host='0.0.0.0', port=4999)
