from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, recipe

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
                # check if user is already in db
                if user.User.check_user_in_db(request.form):
                    return redirect('/')

                else:
                    # save user to db
                    this_user_id = user.User.save_user_to_db(request.form)
                    # save user_data to session
                    this_user = user.User.get_user_by_id(this_user_id)
                    user.User.save_user_to_session(this_user)
                    # send user to next page
                    return redirect('/dashboard')
                

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
                return redirect('/dashboard')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_data' in session: 
        if user.User.validate_success():
            all_recipes = recipe.Recipe.get_all_recipes_with_creators() # get all recipes with creator attached
            if request.method == 'GET':
                print(f"Session >>>>>>>>>>>>>> \n {session}")
                return render_template('dashboard.html', all_recipes = all_recipes)
            
            elif request.method == 'POST':
                return print("How did you get here..?")
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