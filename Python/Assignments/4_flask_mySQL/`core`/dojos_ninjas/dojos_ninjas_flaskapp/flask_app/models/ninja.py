
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Ninja:
    DB = "dojos_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Ninjas Models
    @classmethod
    def save_ninja_to_db(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age)
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)


    # Read Ninjas Models
    @classmethod
    def get_ninjas_by_dojo_id(cls, dojo_id):
        all_ninjas = []
        data = {'dojo_id' : dojo_id}
        query = """SELECT * FROM ninjas
                WHERE dojo_id = %(dojo_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas


    # Update Ninjas Models



    # Delete Ninjas Models