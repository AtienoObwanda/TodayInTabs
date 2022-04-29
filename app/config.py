from distutils.debug import DEBUG


class Config:
    '''
    parent config class
    '''
    pass

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
