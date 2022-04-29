from flask import render_template
from app import app

# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    return render_template('index.html')


@app.route('/news/<news_id>')
def news(news_id):
    '''
    returns the news page
    '''
    return render_template('news.html', id=news_id)