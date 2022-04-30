from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources, get_articles
# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    # Fetching categories ie sports, business and technology:
    technology_articles = get_articles('technology')
    # business = get_sources('business')
    sports_articles= get_articles('sports')
    business_articles = get_articles('business')
    entertainment_articles = get_articles('entertainment')

    sitetitle = 'Today In Tabs- Stay at the top of the headlines...'

    return render_template('index.html',sitetitle=sitetitle, technology = technology_articles, business = business_articles, sports = sports_articles, entertainment=entertainment_articles)




@app.route('/articles/<id>')
def news(id):
    '''
    returns the news page
    '''
    title = 'Today In Tabs- What you missed!'
    return render_template('news.html', id=id, title=title)