import os
class Config:
    '''
    parent config class
    '''
    pass

    # SOURCE_API_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_URL='https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'
    SOURCE_API_URL='https://newsapi.org/v2/top-headlines/sources?category={}&language=en&apiKey={}'
    # API_KEY= os.environ.get('NEWS_API_KEY')


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

config_options = { #dictionary of config options to help us access different configuration option classes
    'development':DevConfig,
    'production':ProdConfig,
}