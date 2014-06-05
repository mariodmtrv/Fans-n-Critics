#!/usr/bin/python3
import json
import urllib.request
import urllib.parse
#from html.parser import HTMLParser
class ReviewCrawler():
    '''
    Performs a website (Google) search for the given movie search and collects the top results
    '''

    def __init__(self):
        self.__urls = []
    @staticmethod
    def __generate_results(search_response):
        results = json.loads(search_response)
        data = results['responseData']
        results = data['results']
        result_urls = []
        for result in results:
           result_urls.append(result['url'])
        if len(result_urls) == 0:
            print ("Failed")
        return result_urls
    def __generate_response(self,query_string):
        query = urllib.parse.urlencode({'q': query_string})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        print(search_results)
        return search_results
    def from_response(self, response_string):
        self.__urls = self.__generate_results(response_string)
    def search_query(self,query):
        enrichments = ['review','movie review']
        for word in enrichments:
            search_response = self.__generate_response(query + word)
            result = self.__generate_results(search_response)
            self.__urls+= result
        # Clear repeating elements
        collected_urls = set(self.__urls)
        self.__urls = list(collected_urls)
    def get_result_url(self, index):
        return self.__urls.__getitem__(index)
