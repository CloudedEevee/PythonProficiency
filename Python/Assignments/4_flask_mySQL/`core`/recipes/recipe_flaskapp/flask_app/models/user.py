
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    DB = "recipe_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []



    # Create Users Models
    @classmethod
    def save_user_to_db(cls, form_data):
        pw_hash = bcrypt.generate_password_hash(form_data['pw'])
        this_user = {
            'first_name' : form_data['first_name'],
            'last_name' : form_data['last_name'],
            'email' : form_data['email'],
            'pw' : pw_hash
            }
        query = """INSERT INTO users (first_name, last_name, email, pw)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"""
        results_id = connectToMySQL(cls.DB).query_db(query, this_user)
        if results_id:
            return results_id
        flash("Something went wrong, please try again.")
        return False
    
    @staticmethod
    def save_user_to_session(this_user):
        user_data = {
                'user_id' : this_user.id,
                'first_name' : this_user.first_name,
                'last_name' : this_user.last_name,
                'email' : this_user.email,
                'pw' : this_user.pw,
                'created_at' : this_user.created_at,
                'updated_at' : this_user.updated_at,
            }
        session['user_data'] = user_data
        print(session['user_data'])
        return True


    @staticmethod
    def validate_user_reg(reg_info):
        # reg_info = Registration info
        is_valid = True
        if not len(reg_info['first_name']) > 2:
            flash("Please enter your first name.")
            is_valid = False
        if not len(reg_info['last_name']) > 2:
            flash("Please enter your last name.")
            is_valid = False
        if not EMAIL_REGEX.match(reg_info['email']):
            flash("Invalid email address.")
            is_valid = False
        ###### pw validation
        if not len(reg_info['pw']) >= 8:
            flash("Invalid password. Must be at least 8 characters.")
            is_valid = False
            ### pw uppercase and num validation
        is_uppercase = False
        is_num = False
        for character in reg_info['pw']:
            if character == character.upper():
                is_uppercase = True
            if character.isnumeric():
                is_num = True
        if not is_uppercase:
            flash("Invalid password. Must have 1 or more uppercase.")
            is_valid = False
        if not is_num:
            flash("Invalid password. Must have 1 or more numbers.")
            is_valid = False
            ### pw confirm validation
        if not reg_info['pw'] == reg_info['pw_confirm']:
            flash("Passwords do not match.")
            is_valid = False
        return is_valid
        



    # Read Users Models
    @classmethod
    def get_all_users(cls):
        all_users = []
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def get_user_by_email(cls, input_data):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL(cls.DB).query_db(query, input_data)
        if not results:
            results = False
            return results
        else:
            return cls(results[0])
    


    @classmethod
    def get_user_by_id(cls, user_id):
        data = { 'user_id' : user_id }
        query = """SELECT * FROM users
                    WHERE id = %(user_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])


    # LOGIN VALIDATION
    @staticmethod
    def validate_user_login(login_info):
        # login_info = request.form, which is a dictionary. 
        is_valid = True
        if not User.get_user_by_email(login_info):
            flash("Invalid Email/Password")
            is_valid = False
        else:
            temp_user = User.get_user_by_email(login_info) #returns cls instance obj from db, if blank: `IndexError: tuple index out of range`
            if not temp_user.email == login_info['email']:
                flash("Invalid Email/Password")
                is_valid = False
            if not bcrypt.check_password_hash(temp_user.pw, login_info['pw']):
                flash("Invalid Email/Password")
                is_valid = False
        return is_valid

    @staticmethod
    def validate_success():
        is_valid = True
        if 'user_data' not in session:
            flash("Please log in.")
            is_valid = False
        return is_valid
    
    @classmethod
    def check_user_in_db(cls, form_data):
        in_db = False
        query = """
                SELECT * FROM users
                WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s
                """
        results = connectToMySQL(cls.DB).query_db(query, form_data)
        if results:
            flash("User already exists. Please login.")
            in_db = True
        return in_db


    # Update Users Models



    # Delete Users Models