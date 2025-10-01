from CreNewsSearch.newsInstance import newsInstance

class NewsSearch():


    newsInstances = {}

    #def __init__(self):
    #  self.translateClasses.append( googleTranslate() )
    #  return None


    def getNewsSearchByLanguage(self, language): 
        if(not language in self.newsInstances):
          self.newsInstances[language] = newsInstance(language)
        return self.newsInstances[language]  

    def search(language, term):
        results = {'status':'none', 'articles':[]}     
        ti = self.getNewsSearchByLanguage(language)
        results = ti.search(term)
        return results


'''
    def getTranslatorByLanguage(self, sourceLanguage,targetLanguage):
        languagePair = sourceLanguage+' -> '+targetLanguage
        if(not languagePair in self.translateInstances):
          self.translateInstances[languagePair] = translateInstance(sourceLanguage,targetLanguage)
        return self.translateInstances[languagePair]  
               

    def translate(sourceLanguage, targetLanguage, sourceText):
        targetText = None      
        ti = self.getTranslatorByLanguage(sourceLanguage,targetLanguage)
        targetText = ti.translate(sourceText)
        return targetText
'''
