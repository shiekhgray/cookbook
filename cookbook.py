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
        cursor.execute('select * from recipes;')
        recipe = cursor.fetchall()
        
    return render_template('view_recipe.html', content=recipe)


if __name__ == "__main__":
    cookbook.run(host='0.0.0.0')
