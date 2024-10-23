from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

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




if __name__ == "__main__":
    app.run(debug=True)