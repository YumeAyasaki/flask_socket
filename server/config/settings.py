class BaseConfig():
    TESTING = False
    DEBUG = False

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db' # Replace with your database URI

class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'