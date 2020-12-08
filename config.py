import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY ='henry'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sokomoko@localhost/henry'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    #email configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitches'
    SENDER_EMAIL = 'henrykanyoro9@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sokomoko@localhost/henry'

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sokomoko@localhost/henry'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}