import json

import requests
import requests_cache


class wrapper:
    def __init__(self):
        self.url='https://restcountries.eu/rest/v2/'
        requests_cache.install_cache('demo_cache')

    def getSpecific(self, country,specificInfo):
        api_url = self.url +'name/'+ country
        response = requests.get(api_url)
        countryInfo=json.loads(response.content)
        return str(specificInfo + "= " + str(countryInfo[0][specificInfo]))

    def getall(self):
        api_url = self.url + 'all'
        response = requests.get(api_url)
        return json.loads(response.content)

    def getalpha(self, country):
        api_url = self.url + 'alpha/' + country
        response = requests.get(api_url)
        return json.loads(response.content)

    def getcurrency(self, country):
        api_url = self.url + 'currency/'+country
        response = requests.get(api_url)
        return json.loads(response.content)

    def getcallingcode(self, country):
        api_url = self.url + 'callingcode/'+country
        response = requests.get(api_url)
        return json.loads(response.content)

    def getcapital(self, country):
        api_url = self.url + 'capital/'+country
        response = requests.get(api_url)
        return json.loads(response.content)

    def getregion(self, country):
        api_url = self.url + 'region/' + country
        response = requests.get(api_url)
        return json.loads(response.content)

    def getName(self, country):
        api_url = self.url+'name/' + country
        response = requests.get(api_url)
        return json.loads(response.content)


