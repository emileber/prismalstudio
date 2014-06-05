servers = {
  'dev': [
    'Emile-Laptop',
  ],
  'prod': [
    'staging', 'vps1', 'vps2', 'vps3'
  ]
}

def get_server_type():
    from socket import gethostname
    server_name = gethostname()
    #print(server_name)
    for server_type, names in servers.items():
        if server_name in names:
            return server_type
    return 'prod' # default



exec("from .%s import *" % get_server_type())
#from .local import *