from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja  #importing the class here
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = Dojo.get_dojos())

@app.route('/ninjas/create' , methods = ['Post'])
def createNinjas():
    data = {}
    data['id'] = request.form['dojos']
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['age'] = request.form['age']
    Ninja.save_ninjas(data)
    return redirect('/ninjas')