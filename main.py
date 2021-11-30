import webapp2
from scraper import PlayStoreScraper
from bs4 import BeautifulSoup
import re
import json

class Home(webapp2.RequestHandler):
    def get(self):
        scraper = PlayStoreScraper()
        data = scraper.getTopCharts()

        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()