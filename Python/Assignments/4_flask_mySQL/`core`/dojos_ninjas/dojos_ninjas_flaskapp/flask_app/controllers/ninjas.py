from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja, dojo # import entire file, rather than class, to avoid circular imports

# Create Ninjas Controller
@app.route('/ninjas', methods=['GET', 'POST'])
def ninjas():
    all_dojos = dojo.Dojo.get_all_dojos()
    if request.method == 'GET':
        return render_template('ninjas.html', all_dojos = all_dojos)
    elif request.method == 'POST':
        ninja.Ninja.save_ninja_to_db(request.form)
        print(request.form)
        return redirect('/dojos/'+str(request.form['dojo_id']))


# Read Ninjas Controller
@app.route('/')
def index():
    return render_template('index.html')


# Update Ninjas Controller



# Delete Ninjas Controller
