
# - System
import os
import urllib
import wsgiref.handlers
import webapp2
# -
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse


page_nav = '''<ul>
  <li><a href="one">One</a></li>
  <li><a href="two">Two</a></li>
</ul>'''

class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
        html_file = 'one.html'

        if path_layer == 'one':
        	  html_file = 'one.html'

        if path_layer == 'two':
        	  html_file = 'two.html'

       # - template
        objects = {
            'page_nav': page_nav,
            
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), html_file)
        self.response.out.write(template.render(path, objects))

app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/one/?', publicSite),
    ('/two/?', publicSite),


], debug=True)
