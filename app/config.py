class Config:
    '''
    parent config class
    '''
    pass
ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
SOURCE_URL= 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    #API_KEY= os.environ.get('NEWS_API_KEY')


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
