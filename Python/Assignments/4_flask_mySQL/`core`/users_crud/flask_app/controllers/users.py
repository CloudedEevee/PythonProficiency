from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports

# Create Users Controller
@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('new_user.html')
    elif request.method == 'POST':
        new_user_id = user.User.save_user_to_db(request.form)
        return redirect('/users/'+str(new_user_id))


# Read Users Controller

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def read_all():
    all_users = user.User.get_all_users()
    return render_template('read_all.html', all_users = all_users)

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def show_user(user_id):
    user_data = user.User.get_user_by_id(user_id)
    return render_template("show_user.html", user_data = user_data)



# Update Users Controller
@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'GET':
        user_data = user.User.get_user_by_id(user_id)
        return render_template("edit_user.html", user_data = user_data, user_id=user_id)
    elif request.method == 'POST':
        user.User.edit_user(request.form)
        return redirect('/users/'+str(user_id))



# Delete Users Controller
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user.User.delete_user_by_id(user_id)
    return redirect('/users')


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