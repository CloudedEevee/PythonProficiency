
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class User:
    DB = "users_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def save_user_to_db(cls, data):
        # what do we tell SQL to do?
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)"""
        # HOW do we get in touch with SQL?
        return connectToMySQL(cls.DB).query_db(query, data)



    # Read Users Models
    @classmethod
    def get_all_users(cls):
        # Clean Python-only variable/list for further manipulation
        # What Variable am I looking to return?
        all_users = []

        # what do we need from MySQL?
        query = "SELECT * FROM users;"

        # MySQL && Python Variable
        results = connectToMySQL(cls.DB).query_db(query)
        
        # How will I add from MySQL/Python into JUST Python?
        for user in results:
            all_users.append(cls(user))
        
        # What will this method return for further use?
        return all_users


    # Update Users Models



    # Delete Users Models


    # ###, DATE_FORMAT(created_at, %M %D %Y) as created_date 