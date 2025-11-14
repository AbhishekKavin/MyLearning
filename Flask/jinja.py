'''
We will be learning about:
    Builidng URL Dynamically using Flask and Jinja
    Variable Rules
    Jinja2 Template Engine
Jinja2 Template Engine : It is a modern and designer-friendly templating language for Python, modeled after Django’s templates. 
It is fast, widely used and secure with the optional sandboxed template execution environment.
{{}} : It is used for expression to print variables or results of expressions.
{% %} : It is used for statements like for loop, if statements etc.
{# #} : It is used for comments in jinja templates.
Flask's render_template function is used to render HTML templates with Jinja2.
Variable Rules : Variable rules are used to define dynamic segments in the URL. 
For example, in the route /user/<username>, <username> is a variable rule that captures the value provided in that segment of the URL.
'''

from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to Jinja Example</H1></>"

@app.route('/index',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}! Your form has been submitted successfully.'
    return render_template('form.html')

## Variable Rules Example
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res = 'You have passed the exam!'
    else:
        res = 'You have failed the exam.'
    return render_template('result.html',results = res)
"""
def success(score):
    return f'The person scored {score}'
"""

@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score>=50:
        res = 'PASS'
    else:
        res = 'FAIL'

    exp = {'Score':score, 'Result':res}
    return render_template('result1.html',results = exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html',results = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result3.html',results = score)

@app.route('/getresult',methods = ['GET','POST'])
def getresult():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        history = float(request.form['History'])
        total_score = (science + maths + history) / 3
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score))




if __name__ == '__main__':
    app.run(debug=True)