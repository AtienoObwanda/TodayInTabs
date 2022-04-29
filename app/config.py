class Config:
    '''
    parent config class
    '''
    pass

NEWS_BASE_URL = "https://newsapi.org/v2/{}?apiKey={}"
ARTICLE_BASE_URL= "https://newsapi.org/v2/everything?sources={}&apiKey={}"
# API_KEY= os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production config class
    '''
    pass

class DevConfig(Config):
    '''
    Development config class
    '''
DEBUG = True
