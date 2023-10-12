
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Friend:
    DB = "first_flask" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name, last_name, occupation) 
                VALUES (%(first_name)s, %(last_name)s, %(occupation)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)



    # Read Users Models
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends

    @classmethod
    def get_friend_by_id(cls, id):
        query = """SELECT * FROM friends 
                WHERE id = %(id)s"""
        data = {'id': id}
        results = connectToMySQL(cls.DB).query_db(query, data)

        # "return the instance of the class found within the results, index of 0"
        return cls(results[0])


    # Update Users Models


    # Delete Users Models