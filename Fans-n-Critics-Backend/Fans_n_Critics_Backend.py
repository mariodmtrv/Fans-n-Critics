from DescriptionProvider import DescriptionProvider
from IMDBRatingEngine import IMDBRatingEngine
dp = DescriptionProvider ("tt0071853")
print(dp.get_name())
ls = dp.get_genre_list()
for x in ls:
    print(x)
rt = IMDBRatingEngine("tt0071853")
print(rt.rating)
print(rt.votes_count)