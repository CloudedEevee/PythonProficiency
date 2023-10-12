from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports

# Create Users Controller



# Read Users Controller

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        if request.form['which_form'] == 'register':
            # invalid registration inputs
            if not user.User.validate_user_reg(request.form):
                return redirect('/')
            # valid reg_inputs
            else:
                # save user to db
                user_id = user.User.save_user_to_db(request.form)
                # save user_data to session
                this_user = user.User.get_user_by_id(user_id)
                user.User.save_user_to_session(this_user)
                # send user to next page
                return redirect('/success')
        elif request.form['which_form'] == 'login':
            # invalid login inputs
            if not user.User.validate_user_login(request.form):
                return redirect('/')
            # valid login_inputs
            else:                
                # get user_data, save to session
                this_user = user.User.get_user_by_email(request.form)
                user.User.save_user_to_session(this_user)
                # send user to next page
                return redirect('/success')



@app.route('/success', methods=['GET','POST'])
def success():
    if user.User.validate_success():
        if request.method == 'GET':
            return render_template('success.html')
        elif request.method == 'POST':
            return redirect('/logout')
    else:
        return redirect('/')

# Update Users Controller



# Delete Users Controller
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

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