'''
Created on 2014-06-04

@author: Emile
'''
# from django import template
# 
# register = template.Library()

from django import template

register = template.Library()

def active(request, pattern):
    if pattern == request.path:
        return 'pure-menu-selected'
    return ''







register.simple_tag(active)