class config:
    '''
    Parent class for the general configuration
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    
class ProdConfig(config):
    '''
    Production Configuration class
    '''
    pass

class DevConfig(config):
    '''
    Development Configurtion class
    '''

    DEBUG = True
