
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Dojo:
    DB = "dojos_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Dojos Models
    @classmethod
    def save_dojo(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES (%(name)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)


    # Read Dojos Models
    @classmethod
    def get_all_dojos(cls):
        # "Ticket for all_dojos!!"
        all_dojos = []

        # What do I need to ask for?
        query = "SELECT * FROM dojos;"

        # Gotcha. HEY SQL!! For this class in this db, I have a question.
        # What's your question?
        # Here's the question...
        results = connectToMySQL(cls.DB).query_db(query)

        # Alright, lemme write this down... one at a time so I don't miss any
        for dojo in results:
            all_dojos.append(cls(dojo))

        # Hey, Chef! Ticket for all_dojos is done! Here you go:
        return all_dojos


    @classmethod
    def get_dojo_by_id(cls, dojo_id):
        data = {'dojo_id' : dojo_id}
        query = """SELECT * FROM dojos
                WHERE id = %(dojo_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])




    # Update Dojos Models



    # Delete Dojos Models