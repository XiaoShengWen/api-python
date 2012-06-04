import urllib2
import httplib
from urlparse import urlparse

"""
This file is part of the domaintoolsAPI_python_wrapper package.
For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

class RestService(object):

    def __init__(self, content_type='json', options={}):

        self.options      = options
        self.content_type = content_type
        self.status_code  = 200

    def get(self, url, proxy=None):

        
        if proxy == None :
            parts = urlparse(url)

            connection = httplib.HTTPConnection(parts.netloc)

            connection.request('GET',parts.path+'?'+parts.query)

            response = connection.getresponse()

            self.status_code = response.status
        else:
            proxy = urllib2.ProxyHandler({'http': proxy})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            response = urllib2.urlopen(url)
            self.status_code = response.code
		
        
        return response.read()
        

    def get_status(self):
        return self.status_code

