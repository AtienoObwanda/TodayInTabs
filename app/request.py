from app import app
import urllib.request, json
from .models import Source, Article #classes created earlier



# Getting api key

api_key = app.config['NEWS_API_KEY']

    #   Getting the article url
source_url = app.config["SOURCE_API_URL"]

    # Getting the articles url
article_url = app.config["ARTICLES_URL"]
    # Getting articles
articles_url = app.config["ARTICLES_URL"]


def get_articles(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_articles_url = article_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results_articles(article_results_list)


    return article_results

def process_results_articles(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        article_list: A list of dictionaries that contain article details
    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:

            article_object = Article(source,author,title,urlToImage,url,description,publishedAt,content)
            article_results.append(article_object)

    return article_results  

def get_sources(category):
    '''
    Function that gets the sources for a given category
    '''
    get_sources_url = source_url.format(category,api_key)

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
        if name:    
            source_object = Source(id,name,description,url,category,country,language)
            source_results.append(source_object)
    return source_results
  









