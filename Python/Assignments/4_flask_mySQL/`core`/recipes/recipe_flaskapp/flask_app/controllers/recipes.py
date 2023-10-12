from flask_app import app
from flask import render_template, redirect, request, session, url_for
from flask_app.models import recipe, user # import entire file, rather than class, to avoid circular imports

# Create Recipes Controller
@app.route('/recipes/create', methods=['GET', 'POST'])
def create_recipe():
    if user.User.validate_success():
        if request.method == 'GET':
            return render_template('create_recipe.html')
        else:
            print("How did you get here?")
    else:
        return redirect('/')

@app.route('/recipes/create/process', methods=['POST'])
def process_recipe():
    if user.User.validate_success():
        if recipe.Recipe.validate_recipe(request.form):
            print(f"recipe form submission is: {request.form}")
            if recipe.Recipe.save_recipe_to_db(request.form):
                return redirect('/dashboard')
            else:
                return redirect('/recipes/create')
        else:
            print("invalid recipe")
            return redirect('/recipes/create')
    else:
        return redirect('/')





# Read Recipes Controller
@app.route('/recipes/view/<int:recipe_id>')
def view_recipe(recipe_id):
    if user.User.validate_success():
        this_recipe = recipe.Recipe.get_recipe_by_id_with_creator(recipe_id)
        this_recipe.created_at = this_recipe.created_at.strftime('%B %e, %Y')
        return render_template('view_recipe.html', this_recipe = this_recipe)
    else:
        return redirect('/')




# Update Recipes Controller
@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if user.User.validate_success():
        this_recipe = recipe.Recipe.get_recipe_by_id_with_creator(recipe_id)
        this_recipe.created_at = this_recipe.created_at.strftime('%Y-%m-%d')
        return render_template('edit_recipe.html', this_recipe = this_recipe, recipe_id = recipe_id)
    else:
        return redirect('/')

@app.route('/recipes/edit/<int:recipe_id>/process', methods=['POST'])
def submit_edit_recipe(recipe_id):
    if recipe.Recipe.validate_recipe(request.form):
        recipe.Recipe.edit_recipe(recipe_id, request.form)
        return redirect('/dashboard')
    else:
        return redirect(url_for('edit_recipe', recipe_id = recipe_id))

# Delete Recipes Controller
@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    recipe.Recipe.delete_recipe(recipe_id)
    return redirect('/dashboard')



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