from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quotes

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'TheVoid.com'
    message = 'Blog Gang Rise UP!!!'
    quotes = get_quotes()
    return render_template('index.html', message = message, title = title, quotes=quotes)