# -*- coding: utf-8 -*-

"""
    Flask Configuration
"""
HOST = '0.0.0.0'
PORT = 9000
DEBUG = True
SECRET_KEY = 'SuperSecretString'

"""
    Logging Configuration
"""
LOG_FILE = 'webapp.log'
LOG_LEVEL = 'DEBUG'

"""
    Database Configuration
"""
DB_USER = ''
DB_PASS = ''
DB_NAME = ''
DB_HOST = ''
DB_CREATED = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + ':3306/' + DB_NAME

"""
    Mail Configuration
"""
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

"""
    Site Configuration
"""
DOMAIN_NAME = 'example.com'
SITE_NAME = 'Flask-Boilerplate'
SITE_ICON = 'icon-code'

CONTACT_MAIL = 'info@' + DOMAIN_NAME
COPYRIGHT_NOTICE = '&copy; 2013 ' + DOMAIN_NAME.lower() + ', all rights reserved.'
COPY_MAIL = 'timh.bergstrom@gmail.com'
