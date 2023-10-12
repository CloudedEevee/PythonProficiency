from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import friend # import entire file, rather than class, to avoid circular imports

# Create Friends Controller



# Read Friends Controller

@app.route('/')
def index():
    all_friends = friend.Friend.get_all()
    return render_template('index.html', all_friends = all_friends)

@app.route('/friends/create_friend')
def create_friend():
    return render_template("create_friend.html")

@app.route('/friends/add_friend', methods=["POST"])
def add_friend():
    friend.Friend.save(request.form)
    return redirect('/')


# Update Friends Controller



# Delete Friends Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.