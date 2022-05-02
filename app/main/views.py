from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles,get_article


# creating views

@main.route('/')
def index():
    '''
    Display the top sources for different categories
    '''
# Fetching sources
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    title = 'Today In Tabs- Top sources'

    return render_template('index.html',title=title,business=business_sources,technology=technology_sources,
    sports=sports_sources,entertainment=entertainment_sources,health=health_sources, science=science_sources )

@main.route('/articles/')
def articles():
    '''
    View root page function for returning index page information
    '''
    # Fetching article categories ie sports, business and technology:
    technology_articles = get_articles('technology')
    sports_articles= get_articles('sports')
    business_articles = get_articles('business')
    entertainment_articles = get_articles('entertainment')
    


    title = 'Today In Tabs- Stay at the top of the headlines...'

    return render_template('articles.html',title=title, technology = technology_articles, 
    business = business_articles, sports = sports_articles, 
    entertainment=entertainment_articles)


@main.route('/source/<id>')
def article(source):
    '''
    returns the news page
    '''
    article_source = get_article(source.name)
    title = 'Today In Tabs- {id}'
    return render_template('article.html',title = title, article = article_source)

