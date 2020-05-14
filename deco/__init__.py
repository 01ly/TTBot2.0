
from req import send_request
from tools import get_header

def fetch(func):
    def wrapper(self,*args,**kwargs):
        config = func(self,*args,**kwargs)
        method = config.get('method','get')
        url = config.get('url')
        params = config.get('params',{})
        data = config.get('data',{})
        _kwargs = config.get('kwargs',{})
        version = config.get('version',700)
        headers = config.get('headers')
        Headers = headers if headers else get_header(int(version))
        response = send_request(method,url,
                                params=params,
                                headers=Headers,
                                data=data,**_kwargs)
        ret = response.json()
        return ret
    return wrapper