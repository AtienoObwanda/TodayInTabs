from app import app
import urllib.request, json
from .models import Source, Article #classes created earlier

#getting apiKey
api_key = app.config['API_KEY']

#getting the articles & news
article_url = app.config['ARTICLE_BASE_URL']
source_url = app.config['SOURCE_BASE_URL']

def get_article(article): #function that takes in article as argument
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
            article_results = process_results(article_results_list)

        return article_results

