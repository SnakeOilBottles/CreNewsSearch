from unittest import TestCase

from CreNewsSearch.NewsSearch import NewsSearch 

class TestSearch(TestCase):
    def test_simple_search(self):
        ns = NewsSearch()
        li = ns.getNewsSearchByLanguage('en')
        tarTree = li.search('climate change')
        print(tarTree)
        #self.assertEqual('Baum', tarTree)
        tarHouse = li.search('earthquake')
        print(tarHouse)
        #self.assertEqual('Haus', tarHouse)

