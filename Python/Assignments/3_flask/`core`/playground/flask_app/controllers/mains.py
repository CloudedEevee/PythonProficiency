from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import main # import entire file, rather than class, to avoid circular imports

# Create Users Controller



# Read Users Controller

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', defaults={'num' : 3, 'color' : "royalblue"}, methods=['GET', 'POST'])
@app.route('/play/<int:num>', defaults={'color' : "royalblue"}, methods=['GET', 'POST'])
@app.route('/play/<int:num>/<string:color>', methods=['GET', 'POST'])
def play(num, color):
    if not request.form:
        flash("Please check the terminal")
        print(">>>>>>>>>> MESSAGE INCOMING <<<<<<<<<< \nI see you're avoiding the form. I worked hard on that, you know. \n... \n... \n... \n-sigh- So be it, just make sure you test the form as well, okay? \n>>>>>>>>>> MESSAGE END <<<<<<<<<<")
    elif request.form['num'] and not request.form['color']:
        num = int(request.form['num'])
    elif request.form['color'] and not request.form['num']:
        color = request.form['color']
    elif request.form['num'] and request.form['color']:
        num = int(request.form['num'])
        color = request.form['color']
    return render_template('play.html', num = num, color = color)

# Update Users Controller



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
# path 	-Like string but accepts slashes