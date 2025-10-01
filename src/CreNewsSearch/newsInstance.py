#from libraries.NewsSearch.freeNews import freeNews
from CreNewsSearch.newsApi import newsApi
import random

##!store and load current stati of instances in csv file (load factor/capacity/workload%)
# also success/failure-rate  -> 100%   new = new*0.95+curr*0.05
# also mean delivery                   new = new*0.95+curr*0.05 
          
class newsInstance():

    newsClasses = []
  
    def __init__(self, language):
      self.language = language
      if(not newsInstance.newsClasses):
          print('Init all news feeds once')
          ## newsInstance.newsClasses.append( freeNews() )
          newsInstance.newsClasses.append( newsApi() )
          # add more   

      self.newsInstances = []
      for newsClass in newsInstance.newsClasses:
        print("init instance")
        print(language)
        print(newsClass.languages)
        if(language in newsClass.languages): 
          print("language found") 
          self.newsInstances.append( newsClass )
      return None

    def search(self, searchTerm):
        foundNews = {}
        print("started instance search")  
        if(self.newsInstances):
          print("inside instance search") 
          anyNewsSearch = random.choice(self.newsInstances)
          foundNews = anyNewsSearch.search(searchTerm, self.language)      
        return foundNews

    def getNewsSearchInfo():
      for newsClass in newsInstance.newsClasses:
        print(newsClass.getServiceName())
        print(['counter: ',newsClass.callCounter, 'total:',newsClass.totalNewsCounter])  


'''  
    def __init__(self, sourceLanguage,targetLanguage):
      self.sourceLanguage = sourceLanguage
      self.targetLanguage = targetLanguage
      if(not translateInstance.translateClasses):
          print('Init all translators once')
          translateInstance.translateClasses.append( googleTranslate() )
          # add more

      self.translateInstances = []
      for translateClass in translateInstance.translateClasses:
        if((sourceLanguage in translateClass.sourceLanguages) and (targetLanguage in translateClass.targetLanguages)): 
          self.translateInstances.append( translateClass )
      return None

    def translate(self, sourceText):
        targetText = None
        if(self.translateInstances):
          anyTranslator = random.choice(self.translateInstances)
          targetText = anyTranslator.translate(sourceText, self.sourceLanguage, self.targetLanguage)      
        return targetText

    def getTranslatorInfo():
      for translateClass in translateInstance.translateClasses:
        print(translateClass.getServiceName())
        print(['counter: ',translateClass.callCounter, 'len:',translateClass.totalTextLength])       
'''
                
