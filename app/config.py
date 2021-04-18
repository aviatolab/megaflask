class Configuration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:500$Tyuiop500@127.0.0.1/denisov?auth_plugin' \
                              '=mysql_native_password'
    SECRET_KEY = 'something very secret'

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'


