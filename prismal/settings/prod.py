'''
Created on 2014-06-05

@author: Emile
'''
from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1', 
    '.prismalstudio.herokuapp.com',
    '.prismalstudio.com',
]

MIDDLEWARE_CLASSES += (
    # prevent loading the site in an Iframe.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

X_FRAME_OPTIONS = 'SAMEORIGIN' # or DENY