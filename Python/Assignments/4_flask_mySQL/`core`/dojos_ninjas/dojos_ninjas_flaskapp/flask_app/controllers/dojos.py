from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo, ninja # import entire file, rather than class, to avoid circular imports

# Create Dojos Controller
@app.route('/dojos/new', methods=['POST'])
def dojos_new():
    dojo.Dojo.save_dojo(request.form)
    return redirect('/dojos')


# Read Dojos Controller
@app.route('/dojos', methods=['GET', 'POST'])
def dojos():
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo_data = dojo.Dojo.get_dojo_by_id(dojo_id)
    print(dojo_data)
    all_ninjas = ninja.Ninja.get_ninjas_by_dojo_id(dojo_id)
    print(all_ninjas)
    return render_template("show_dojo.html", dojo_data = dojo_data, all_ninjas = all_ninjas)
    


# Update Dojos Controller



# Delete Dojos Controller
