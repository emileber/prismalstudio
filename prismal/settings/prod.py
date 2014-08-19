'''
Created on 2014-06-05

@author: Emile
'''
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1', # staticfile handling specificly doesn't work on debug false
    '.prismalstudio.herokuapp.com',
    '.prismalstudio.com',
]

ALLOWED_HOSTS = ['*']

MIDDLEWARE_CLASSES += (
    # prevent loading the site in an Iframe.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

X_FRAME_OPTIONS = 'SAMEORIGIN' # or DENY