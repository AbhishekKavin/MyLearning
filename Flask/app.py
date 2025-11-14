from flask import Flask
'''
Crete a Flask application instance which will be WSGI (Web Server Gateway Interface) compliant.
This instance will be used to handle incoming web requests and route them to the appropriate view functions.
'''
# WSGI Application Instance
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Test Flask Application.This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to index page of Flask Application"

if __name__ == '__main__':
    app.run(debug = True)