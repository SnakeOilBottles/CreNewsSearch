from unittest import TestCase

from CreNewsSearch.NewsSearch import NewsSearch 

class TestSearch(TestCase):
    def test_simple_search(self):
        ns = NewsSearch()
        li = ns.getNewsSearchByLanguage('en')
        resCC = li.search('climate change')
        #print(resCC)
        self.assertEqual('OK', resCC['status'])
        self.assertTrue(len(resCC['articles'])>0)
        resEQ = li.search('earthquake')
        #print(resEQ)
        self.assertEqual('OK', resEQ['status'])
        self.assertTrue(len(resEQ['articles'])>0)

