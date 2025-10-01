#pip3 install CreNewsSearch

#import mysecrets
from CreNewsSearch.NewsSearch import NewsSearch 

from CreNewsSearch.newsInstance import newsInstance

## TODO: remove!
import os
if(not os.getenv('NEWSAPI_KEY')):
    os.environ['NEWSAPI_KEY'] = '561d14bba2984f0bb68dc215cfaea814'


ns = NewsSearch()
li = ns.getNewsSearchByLanguage('en')
tar = li.search('tree')
print(tar)
tar2 = li.search('house')
print(tar2)

newsInstance.getNewsSearchInfo()


