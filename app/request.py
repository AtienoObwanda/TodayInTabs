from app import app
import urllib.request, json
from .models import Source, Article #classes created earlier


#getting apiKey

api_key = app.config['NEWS_API_KEY']

#getting the articles & news
article_url = app.config['ARTICLE_BASE_URL']
source_url = app.config['SOURCE_BASE_URL']


def get_sources(category):
    '''
    Function that gets the sources for a given category
    '''
    get_sources_url = source_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results_sources(source_results_list)

        return source_results

def process_results_sources(source_list):
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
    source_object = Source(id,name,description,url,category,country,language)
    source_results.append(source_object)
    return source_results
  



def get_article(id): #function that takes in article as argument
    '''
    Function that gets the json response to the article request
    '''
    get_articles_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results_articles(article_results_list)

        return article_results

def process_results_articles(article_list):
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        img = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if img:
            article_object = Article(id,author, title, description, url,img,date)
            article_results.append(article_object)
    return article_results





