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
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True