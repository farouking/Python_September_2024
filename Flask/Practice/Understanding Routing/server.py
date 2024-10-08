from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def Dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')          # 3rd Task
def say(name):
    return f"Hi {name.capitalize()}!"

#  # 4rd Task
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

#  # Ninja Bonus 1
@app.route('/say2/<name>')  # Ninja Bonus
def say2(name):
    if name.isalpha():
        return f"Hi {name.capitalize()}!"
    else:
        return "Type Error: input must be a string containing only alphabetic characters"

#  # Ninja Bonus 2
@app.route('/repeat_word2/<int:num2>/<word2>')
def repeat_word2(num2, word2):
    output = ''
    if num2 > 0 and isinstance(word2, str) and word2.isalpha():
        for i in range(num2):
            output += f"<p>{word2}</p>"
        return output
    else:
        return "Type Error: Check your input. 'num2' must be a positive integer and 'word2' must be a string containing only alphabetic characters."




if __name__=="__main__":
    app.run(debug=True)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=5000)    # Run the app in debug mode.

