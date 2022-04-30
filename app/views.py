from flask import render_template
from app import app
from .request import get_sources
# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    # Fetching categories ie sports, business and technology:

    technologySources = get_sources('technology')
    businessSources = get_sources('business')
    sportSources = get_sources('sports')


    title = 'Today In Tabs- Stay at the top of the headlines...'


    return render_template('index.html',title=title, technology = technologySources, business = businessSources, sport = sportSources)


@app.route('/articles/<id>')
def news(id):
    '''
    returns the news page
    '''
    title = 'Today In Tabs- What you missed!'
    return render_template('news.html', id=id, title=title)