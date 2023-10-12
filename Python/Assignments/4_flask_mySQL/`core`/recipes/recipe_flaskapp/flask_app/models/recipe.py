
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import user
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Recipe:
    DB = "recipe_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    # Create Recipes Models
    @classmethod
    def save_recipe_to_db(cls, form_data):
        this_recipe = {
            'name' : form_data['name'],
            'under_30' : form_data['under_30'],
            'description' : form_data['description'],
            'instructions' : form_data['instructions'],
            'created_at' : form_data['created_date'],
            'creator' : session['user_data']['user_id']
            }
        query = """INSERT INTO recipes (name, under_30, description, instructions, created_at, user_id)
                VALUES (%(name)s, %(under_30)s, %(description)s, %(instructions)s,  %(created_at)s, %(creator)s);"""
        results_id = connectToMySQL(cls.DB).query_db(query, this_recipe)
        if results_id:
            return results_id
        flash("Something went wrong, please try again.")
        return False

    @classmethod
    def get_recipe_by_id_with_creator(cls, recipe_id):
        data = { 'recipe_id' : recipe_id}
        query = """
                SELECT * FROM recipes
                LEFT JOIN users
                    ON recipes.user_id = users.id
                WHERE recipes.id = %(recipe_id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for row in results:
            this_recipe = cls(row)
            # store the creator data
            recipe_creator_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'pw' : row['pw'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            # create cls instance of creator data
            this_creator = user.User(recipe_creator_data)
            # add creator to recipe
            this_recipe.creator = this_creator
        return this_recipe





    # Read Recipes Models
    @classmethod
    def get_all_recipes_with_creators(cls):
        all_recipes = []
        query = """
                SELECT * FROM recipes
                LEFT JOIN users
                    ON recipes.user_id = users.id;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        for row in results:
            this_recipe = cls(row)
            # store the creator data
            recipe_creator_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'pw' : row['pw'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            # create cls instance of creator data
            this_creator = user.User(recipe_creator_data)
            # add creator to recipe
            this_recipe.creator = this_creator
            # append to all_recipes
            all_recipes.append(this_recipe)
        return all_recipes

    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if not len(form_data['created_date']) > 0 or not len(form_data['under_30']) > 0:
            flash("All fields must be completed.")
            is_valid = False
        if not len(form_data['name']) > 3:
            flash("Name must have at least 3 characters.")
            is_valid = False
        if not len(form_data['description']) > 3:
            flash("Description must have at least 3 characters.")
            is_valid = False
        if not len(form_data['instructions']) > 3:
            flash("Instructions must have at least 3 characters.")
            is_valid = False
        return is_valid





    # Update Recipes Models
    @classmethod
    def edit_recipe(cls, recipe_id, form_data):
        data = {
            'recipe_id' : recipe_id,
            'name' : form_data['name'],
            'under_30' : form_data['under_30'],
            'description' : form_data['description'],
            'instructions' : form_data['instructions'],
            'created_at' : form_data['created_date']
        }
        query = """
                UPDATE recipes
                SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, created_at = %(created_at)s
                WHERE id = %(recipe_id)s
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results





    # Delete Recipes Models
    @classmethod
    def delete_recipe(cls, recipe_id):
        data = {'recipe_id' : recipe_id}
        query = """DELETE FROM recipes 
                    WHERE id = %(recipe_id)s"""
        return connectToMySQL(cls.DB).query_db(query, data)




