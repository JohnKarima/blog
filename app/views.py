from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Blog Gang Rise UP!!!'
    title = 'TheVoid.com'
    return render_template('index.html', message = message, title = title)