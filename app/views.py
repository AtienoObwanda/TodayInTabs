from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources, get_articles
# creating views
@app.route('/')
def index():
    '''
    View root page function for returning index page information
    '''
    # Fetching article categories ie sports, business and technology:
    technology_articles = get_articles('technology')
    sports_articles= get_articles('sports')
    business_articles = get_articles('business')
    entertainment_articles = get_articles('entertainment')
    top_sources = get_sources('us')

    title = 'Today In Tabs- Stay at the top of the headlines...'

    return render_template('index.html',title=title, technology = technology_articles, 
    business = business_articles, sports = sports_articles, 
    entertainment=entertainment_articles, us=top_sources)

@app.route('/sources/')
def sources():
    '''
    Display the top sources for different categories
    '''
# Fetching sources
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    title = 'Today In Tabs- Top sources'

    return render_template('sources.html',title=title,business=business_sources,technology=technology_sources,
    sports=sports_sources,entertainment=entertainment_sources )

@app.route('/articles/<id>')
def news(id):
    '''
    returns the news page
    '''
    title = 'Today In Tabs- What you missed!'
    return render_template('news.html', id=id, title=title)