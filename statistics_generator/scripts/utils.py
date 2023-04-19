import datetime

from sshtunnel import SSHTunnelForwarder


def get_today_file_name(prefix='', postfix='', extension=''):
    today = datetime.datetime.today()
    today = today.strftime('%Y%m%d')        
    output_file_name = prefix + today + postfix + '.' + extension
    return output_file_name
    
    
class SingletonClass:
    __instance = None

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__get_instance
        return cls.__instance


class SSHTunnel:
    def __init__(self, ssh_host, ssh_username, ssh_pkey, remote_bind_address):
        self.tunnel = SSHTunnelForwarder(
            (ssh_host, 22), ssh_username=ssh_username,
            ssh_pkey=ssh_pkey, 
            remote_bind_address=remote_bind_address
        )
    
    def __enter__(self):
        self.tunnel.start()
        return self.tunnel
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.tunnel.close()
         
    def start(self):
        print('create tunnel')
        self.tunnel.start()
    
    def stop(self):
        print('start tunnel')
        self.tunnel.stop()

