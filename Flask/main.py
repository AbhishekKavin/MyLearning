from flask import Flask,render_template
'''
Crete a Flask application instance which will be WSGI (Web Server Gateway Interface) compliant.
This instance will be used to handle incoming web requests and route them to the appropriate view functions.
'''
# WSGI Application Instance
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Test Flask Application</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True)