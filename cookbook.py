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
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.mysql import MySQL

mysql = MySQL()
 

#######
# create Flask app
#######
cookbook = Flask(__name__)

cookbook.config.update(dict(
    DEBUG=True
))

# MySQL config
cookbook.config['MYSQL_DATABASE_USER'] = 'recipes'
cookbook.config['MYSQL_DATABASE_PASSWORD'] = 'WbGM6OMZ6QgVYrCM'
cookbook.config['MYSQL_DATABASE_DB'] = 'Cookbook'
cookbook.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(cookbook)


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
    return render_template('view_recipe.html')


if __name__ == "__main__":
    cookbook.run(host='0.0.0.0')
