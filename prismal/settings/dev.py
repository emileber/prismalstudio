'''
Created on 2014-06-05

@author: Emile
'''
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'debug_toolbar',
)