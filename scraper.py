from bs4 import BeautifulSoup
import requests
import re
import json

class PlayStoreScraper:

    def getTopCharts(self):

        url = "https://play.google.com/store/apps/top?hl=en&gl=IN"

        # get the html
        res = requests.get(url)
        htmlContent = res.content
        # print(htmlContent)
        # print("content available")

        # parse the html
        soup = BeautifulSoup(htmlContent, 'html.parser')

        # title
        title = soup.title.text

        #App Links
        appLinks = soup.find_all('a',class_="poRVub");

        # collections
        collections = soup.find_all('h2')

        # App names
        apps = soup.find_all('div', class_="WsMG1c nnK0zc")

        # Developer names
        developersList = soup.find_all('div', class_="KoLSrc")
        developersList = developersList[::2]

        # Ratings of apps
        ratings = soup.find_all('div', class_="pf5lIe")
        print(title, "\n")

        obj = {}
        listInd = 0

        for collection in collections:

            appsList = []
            start = listInd
            end = listInd + 10
            for i in range(start, end):
                app = {}
                app["Link"] = "https://play.google.com" + appLinks[i].get("href")
                app["Name"] = apps[i].text
                app["Developer"] = developersList[i].text
                app["Rating"] = ratings[i].div.get("aria-label")
                appsList.append(app)
                listInd += 1

            obj[collection.text] = appsList

        return obj

