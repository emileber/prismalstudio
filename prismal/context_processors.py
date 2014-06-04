'''
Created on 2014-06-04

@author: Emile
'''
from django.conf import settings


def solid_i18n(request):
    example_vars = {
        'SOLID_I18N_USE_REDIRECTS': settings.SOLID_I18N_USE_REDIRECTS,
        'LANGUAGE_DEFAULT': settings.LANGUAGE_CODE,
    }
    return {"solid_i18n": example_vars}