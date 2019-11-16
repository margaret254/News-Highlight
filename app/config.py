class config:
    '''
    Parent class for the general configuration
    '''

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
