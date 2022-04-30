from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources
# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    # Fetching categories ie sports, business and technology:
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')


    title = 'Today In Tabs- Stay at the top of the headlines...'


    return render_template('index.html',title=title, technology = technology_sources, business = business_sources, sports = sports_sources)


@app.route('/articles/<id>')
def news(id):
    '''
    returns the news page
    '''
    title = 'Today In Tabs- What you missed!'
    return render_template('news.html', id=id, title=title)