#!/usr/bin/python3
import json
import urllib.request
import urllib.parse
#from html.parser import HTMLParser
class WebCrawler():
    '''
    Performs a Google search for the given movie search and collects the top results
    '''

    def __init__(self, query):
        self.__query = query
        self.__generate_results()

    def __generate_results(self):
        query = urllib.parse.urlencode({'q': self.__query})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        print(url)
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        results = json.loads(search_results)
        data = results['responseData']
        results = data['results']
        self.__urls = []
        for result in results:
            self.__urls.append(result['url'])
        if len(self.__urls) == 0:
            print ("Failed")

    def get_result_url(self, index):
        return self.__urls.__getitem__(index)
