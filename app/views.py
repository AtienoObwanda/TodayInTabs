from flask import render_template
from app import app

# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    return render_template('index.html')
    