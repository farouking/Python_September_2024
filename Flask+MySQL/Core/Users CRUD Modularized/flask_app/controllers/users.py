
from flask import  render_template, request, redirect,session
from flask_app.models.user import User
from flask_app import app

@app.route('/')
def index():
    return render_template("Read (All).html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("Create.html")

@app.route('/user/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {"id": id}
    return render_template("Update.html", user=User.read_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/user/show/<int:id>')
def show(id):
    data = {"id": id}
    return render_template("Read One.html", user=User.read_one(data))

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {"id": id}
    User.delete(data)
    return redirect('/')