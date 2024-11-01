from flask_app import app 
from flask_app.controllers import dojos_controller, ninjas_controller #import  your controller (file name controller.)

if __name__=='__main__':
    app.run(debug=True,port=5000)