from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja 


@app.route('/')
def reroute():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    return render_template('newdojos.html', dojos = Dojo.get_dojos())

@app.route('/dojos/create', methods = ['Post'])
def createDojos():
    print(request.form)
    data = {}
    data['name'] = request.form['name']
    Dojo.save_dojos(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def showDojoNinja(id):
    data_dojo_id = {
        'id' : id
    }
    return render_template('dojos.html', dojo_info_w_ninjas = Ninja.get_dojo_w_ninjas(data_dojo_id))