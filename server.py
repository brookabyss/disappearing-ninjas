from flask import Flask, redirect, render_template, session
app=Flask(__name__)
app.secret_key="12345"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def show():
    return render_template('ninja.html')
@app.route('/ninja/<color>')
def show_color(color):
    if color=="blue":
        session['ninja']= "img/leonardo.jpg"
    elif color=="orange":
        session['ninja']= "img/michelangelo.jpg"
    elif color=="red":
        session['ninja']= "img/raphael.jpg"
    elif color=="purple":
        session['ninja']= "img/donatello.jpg"
    else:
        session['ninja']= "img/notapril.jpg"
    return render_template('color.html')
app.run(debug=True)
