from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports

# Create Users Controller



# Read Users Controller

@app.route('/')
def index():
    if not session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template('index.html')


# Update Users Controller
@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.form['which_button'] == 'plus_one':
        return redirect('/')
    if request.form['which_button'] == 'plus_two':
        session['visits'] += 1
        return redirect('/')
    if request.form['which_button'] == 'choose_inc':
        session['visits'] += (int(request.form['num_inc'])-1)
        return redirect('/')
    if request.form['which_button'] == 'reset':
        session.pop('visits')
        return redirect('/')
    else:
        return print('Something went wrong...')


# Delete Users Controller


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