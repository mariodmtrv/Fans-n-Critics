#!/usr/bin/python3
import json
import urllib.request
import urllib.parse
#from html.parser import HTMLParser


class ReviewCrawler():
    '''
    Performs a website (Google) search with various queries for the given movie and collects the top results
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
            print("Failed")
        return result_urls

    def __generate_response(self, query_string):
        query = urllib.parse.urlencode({'q': query_string})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        return search_results

    def from_response(self, response_string):
        self.__urls = self.__generate_results(response_string)

    def search_query(self, query):
        ENRICHMENTS = ['review', 'movie review', 'complete review']

        for word in ENRICHMENTS:
            search_response = self.__generate_response(query + word)
            result = self.__generate_results(search_response)
            self.__urls += result
        self.cleanup_queries()


    def cleanup_queries(self):
        # Cleans up the repeating urls
        collected_urls = set(self.__urls)
        self.__urls = list(collected_urls)
        # Cleans up the dirty urls containing some known sites
        processed_urls = self.__urls
        self.__urls = []
        FORBIDDEN = ['imdb', 'rottentomatoes', 'metacritic', 'youtube', 'google']
        for url in processed_urls:
            flag = 0
            for forbidden in FORBIDDEN:
                if forbidden in url:
                    flag = 1
                    break
            if flag == 0:
                self.__urls.append(url)

    def get_result_url(self, index):
        return self.__urls.__getitem__(index)

    def get_results_count(self):
        return len(self.__urls)
