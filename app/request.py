from app import app
import urllib.request, json
from .models import Source, Article #classes created earlier

api_key = None
source_url = None
articles_url = None
article_url = None

# Getting api key
def configure_request(app):
    global api_key, source_url,articles_url,article_url
    
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config["SOURCE_API_URL"]
    articles_url = app.config["ARTICLES_URL"]
    article_url = app.config["ARTICLE_BASE_URL"]


def get_articles(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_articles_url = articles_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)


    return articles_results

def process_results_articles(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    '''
    articles_results = []
    for articles_item in articles_list:
        source = articles_item.get('source')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        image = articles_item.get('urlToImage')
        date = articles_item.get('publishedAt')
        content = articles_item.get('content')

        if image:

            articles_object = Article(source,author,title,image,url,description,date,content)
            articles_results.append(articles_object)

    return articles_results  

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
        if name:    
            source_object = Source(id,name,description,url,category,country)
            source_results.append(source_object)
    return source_results



def get_article(sources):
    '''
    Function that gets the json responce to our url request
    '''
    get_article_url = article_url.format(sources,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_details_data = url.read()
        get_article_details_response = json.loads(get_article_details_data)

        article_details_results = None

        if get_article_details_response['articles']:
            article_details_results_list = get_article_details_response['articles']
            article_details_results = process_results_articles(article_details_results_list)


    return article_details_results

def process_results_article(article_details_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    '''
    article_details_results = []
    for article_item in article_details_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        content = article_item.get('content')

        if image:

            article_details_object = Article(source,author,title,image,url,description,date,content)
            article_details_results.append(article_details_object)

    return article_details_results  

