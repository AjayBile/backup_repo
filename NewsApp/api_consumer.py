import requests
import json


class NewsApiParser():

    def __init__(self, url):
        self.url = url

    def getAllData(self):
        response = requests.get(self.url)
        return json.loads(response.text)