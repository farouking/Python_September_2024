from flask import Flask, render_template  
app = Flask(__name__)    

#Level 01
@app.route('/play')
def play():
    return render_template('index.html',times=3)
@app.route('/play/<times>')
def multiple(times):
    return render_template('index.html',times=int(times))

#Level 02 & 03
@app.route('/play/<times>/<color>')
def multiple_and_change(times,color):
    return render_template('index.html',times=int(times),color='style=background-color:'+ color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5000)    # Run the app in debug mode.s
