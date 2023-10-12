from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import main # import entire file, rather than class, to avoid circular imports

######################## Create Mains Controller



######################## Read Mains Controller


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')

@app.route('/say/<string:this_name>', methods=['GET', 'POST'])
def say_something(this_name):
    if request.method == 'POST':
        this_name = request.form['this_name']
        print(type(this_name))
    return render_template('say_something.html', this_name = this_name)


# Process repeat inputs....
@app.route('/repeat', methods=['POST'])
def repeat():
    num = request.form['num']
    phrase = request.form['phrase']
    return redirect(f"/repeat/{num}/{phrase}")

# Redirect to repeat.html
@app.route('/repeat/<int:num>/<string:phrase>')
def repeat_num_phrase(num, phrase):
    return render_template('repeat.html', num = num, phrase = phrase)

# Error Route
@app.errorhandler(404)
def error_404(oh_no):
    return render_template('error.html'), 404

@app.errorhandler(405)
def error_405(oh_no):
    return render_template('error.html'), 40

######################## Update Mains Controller



######################## Delete Mains Controller


######################## Notes:
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