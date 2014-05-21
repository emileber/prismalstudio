'''
Created on 2014-05-18

@author: Emile
'''

#create or update french
#django-admin.py makemessages -l fr

# update
#django-admin.py makemessages -a

#compile 
#django-admin.py compilemessages

import subprocess
status = subprocess.call("django-admin.py makemessages -l fr", shell=True)
print(status)