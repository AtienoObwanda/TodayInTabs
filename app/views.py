from flask import render_template
from app import app

# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    title = 'Today In Tabs- Stay at the top of the headlines...'
    return render_template('index.html',title=title)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    returns the news page
    '''
    title = 'Today In Tabs- What you missed!'
    return render_template('news.html', id=news_id, title=title)