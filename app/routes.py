from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    #return ("Hello World")

    a = "My name is Dishita"
    return """
    <html>
        <head>
            <title> Home </title>
        </head>
        <body>
            <div><a href ="/about"> About </a></div>
            <div><a href ="/test"> Test Page <a></div>
            <div><a href ="/test2"> Test2 Page <a></div>""" +a+ """
       </body>
    </html>
    """
@app.route('/about')
def about():
    return "About"

@app.route('/test')
def test():
    user = {'username': 'Dishita'}
    age = 15
    return render_template('test.html', user=user, age = age)

@app.route('/test2')
def test2():
    user = {'username': 'Calista'}
    sample_data = [
    {
    'author' : {'username': 'Calista'},
    'body' : 'Hello!'   
    },
    {
    'author' : {'username': 'Dishita'},
    'body' : 'Welcome to Flask!'
    },
    {
    'author' : {'username' : 'Angelina'},
    'body' : 'Welcome!'
    }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)


