#from DescriptionProvider import DescriptionProvider
#from IMDBRatingEngine import IMDBRatingEngine
#dp = DescriptionProvider ("tt0071853")
#print(dp.get_name())
#ls = dp.get_genre_list()
#for x in ls:
#    print(x)
#rt = IMDBRatingEngine("tt0071853")
#print(rt.rating)
#print(rt.votes_count)
from movie_data_extraction.Parsers import ReviewParser, WebCrawler

search = WebCrawler("django unchained review")
rev = ReviewParser.extract_review(search.get_result_url(3))
print(rev)
