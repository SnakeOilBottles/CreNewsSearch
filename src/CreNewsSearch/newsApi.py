from CreNewsSearch.NewsBase import NewsBase

import random
import requests
#from urllib.parse import urlparse
import json

#https://newsapi.org/
#https://newsapi.org/docs/errors
# 100 requests/day



class newsApi(NewsBase):
    
    languages = {}
    workload = 0.0 #%0.0-100.0
    callCounter = 0
    totalNewsCounter = 0 
    #maxTextLength = 5000

    def __init__(self):
        languages = {'ar':'ar', 'de':'de', 'en':'en', 'es':'es', 'fr':'fr', 'he':'he', 'it':'it', 
                     'nl':'nl', 'no':'no', 'pt':'pt', 'ru':'ru', 'sv':'sv', 'zh':'zh',
                     '??':'ud',
                     'ja':'jp' #seems to work! but uses toplevel domain
                    }
        newsApi.languages = languages

    def getServiceName(self):
        return 'newsApi'

    def mapStatus(status):
        stateMap = {'200': {'status':'OK', 'action':'none'},
                    '400': {'status':'Bad Request', 'action':'delay'},
                    '401': {'status':'Unauthorized', 'action':'stop'},
                    '429': {'status':'Too Many Requests', 'action':'delay'},
                    '500': {'status':'Server Error', 'action':'delay'},
                    'ok': {'status':'OK', 'action':'none'},
                    'error': {'status':'Bad Request', 'action':'delay'},
                    'apiKeyDisabled': {'status':'Unauthorized', 'action':'stop'},
                    'apiKeyExhausted': {'status':'Unauthorized', 'action':'stop'},
                    'apiKeyInvalid': {'status':'Unauthorized', 'action':'stop'},
                    'apiKeyMissing': {'status':'Unauthorized', 'action':'stop'},
                    'parameterInvalid': {'status':'Bad Request', 'action':'delay'},
                    'parametersMissing': {'status':'Bad Request', 'action':'delay'},
                    'rateLimited': {'status':'Too Many Requests', 'action':'delay'},
                    'sourcesTooMany': {'status':'Bad Request', 'action':'delay'},
                    'sourceDoesNotExist': {'status':'Bad Request', 'action':'delay'},
                    'unexpectedError': {'status':'Server Error', 'action':'delay'},
                   }
        result = {'status':'Unknown', 'action':'delay'}
        if (status in stateMap):
            result = stateMap[status]   
        return result


    def mapArticles(articles):
        return articles


    def search(self, searchTerm, language):
        print("inside search newsapi")
        newsApi.callCounter += 1
        ##
        apiKey = "561d14bba2984f0bb68dc215cfaea814"
        ## add multiple keys! 


        page = random.choice(['1','2','3','4','5'])    #1-3?/or by seldomness... 
        sort = random.choice(['relevancy', 'popularity', 'publishedAt'])
        url = ('https://newsapi.org/v2/everything?'
               'q='+searchTerm+'&'
               'language='+language+'&'
               'page='+page+'&'
               'sortBy='+sort+'&'
               'apiKey='+apiKey
               #'excludeDomains=www.zeit.de,www.reuters.com'
               )
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        #print(response.text)
        #foundNew = False
        #foundZero = True
        print(response.status_code)
        #https://newsapi.org/docs/errors
        #200:ok
        #400:bad request
        #401:missing/wrong api key
        #429:too many requests
        #500:server error
        ## json['status'] -> ok/error
        ### json['code'],json['message']
        state = newsApi.mapStatus(response.status_code)  #200,400,401,429,500
        results = {'status':state['status'], 'articles':[]}    # totalResults
        if(response.text):
          jsonData = json.loads(response.text)
          # https://newsapi.org/docs/errors
          state = newsApi.mapStatus(jsonData['status'])  #ok,error
          results['status'] = state['status']
          if('error'==jsonData['status']):
              print([jsonData['code'],jsonData['message']])
              state = newsApi.mapStatus(jsonData['code'])  #ok,error
              results['status'] = state['status'] 
          else:
              ## newsApi.totalNewsCounter += jsonData['totalResults']         ##
              newsApi.totalNewsCounter += len(jsonData['articles']) 
              results['articles'] = newsApi.mapArticles(jsonData['articles'])
          #handle state['action']  -> i.e. increase counter
        return results


'''
ar, de, en, es, fr, he, it, nl, no, pt, ru, sv, ud, zh
'''

def inqRandomNews():
    apiKey = os.getenv('NEWSAPI_KEY')
    apiKey = 'af24229d673d4b1ab546df8c4ca9f176' ## DELETE!!

    #keyWord = random.choice(searchWords)
    #language = 'de'
    #language = 'en'   
    #language = 'fr' 
    keyWord = random.choice(list(searchWords.keys()))
    language = searchWords[keyWord]
    newLanguage = random.choice(newsapiLanguages)
    if((not newLanguage == language) & (random.uniform(0.0, 100.0)>70.0)):
        print('language: '+language+'; keyword: '+keyWord)
        keyWord = keyWord.strip("'")
        translatorList = []
        # if  GoogleTranslator.get_supported_languages(as_dict=True).values()
        translatorList.append(GoogleTranslator(source=language, target=newLanguage))
        translatorList.append(MyMemoryTranslator(source=language, target=newLanguage))   #-ud(ur?),se(sv?)
        if((not language in ['ar','he','no','se','ud','ur']) and (not newLanguage in ['ar','he','no','se','ud','ur'])):
            translatorList.append(LingueeTranslator(source=language, target=newLanguage))
        #Yandex, Deepl, QCRI needs API
        someTranslator = random.choice(translatorList)
        try:
            newKeyWord = someTranslator.translate(keyWord)
            keyWord = "'" + newKeyWord + "'"
            language = newLanguage
        except deep_translator.exceptions.ElementNotFoundInGetRequest as e:
            print(['ElementNotFoundInGetRequest', e])
        except:
            print("Some exception in keyword translate - keep")
    if(not 'xx'==language):
        #searchWords.pop(keyWord)

        page = random.choice(['1','2','3','4','5'])  
        #page = '1'
        sort = random.choice(['relevancy', 'popularity', 'publishedAt'])
        #sort = 'relevancy'

        print('language: '+language+'; keyword: '+keyWord+'; Page: '+page)
        # https://newsapi.org/docs/endpoints/everything
        url = ('https://newsapi.org/v2/everything?'
            'q='+keyWord+'&'
            'language='+language+'&'
            'page='+page+'&'
            'sortBy='+sort+'&'
            'apiKey='+apiKey
            #'excludeDomains=www.zeit.de,www.reuters.com'
            )
            
            # sortBy=relevancy   : relevancy, popularity, publishedAt
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        #print(response.text)
        foundNew = False
        foundZero = True
        if(response.text):
            jsonData = json.loads(response.text)
            #see climate change....
            if (('ok'==jsonData['status']) and (jsonData['totalResults']>0)):
                foundZero = False
                for article in jsonData['articles']:
                    title = article['title']
                    description = article['description']
                    url = article['url']
                    #later use list...
                    url = url.replace('https://www.zeit.de/zustimmung?url=', '')
                    url = url.replace('https://www.golem.de/sonstiges/zustimmung/auswahl.html?from=', '')
                    url = url.replace('%3A', ':')
                    url = url.replace('%2F', '/')                

                    domain = urlparse(url).netloc

                    image = article['urlToImage']
                    published = article['publishedAt']
                    content = article['content']
                    print(article)



                    data = {'url':url, 'valid':0, 'domain':domain, 'en':'', 'published':published, 'description':description, 'title':title,
                           'image':image, 'content':content, 'language': language, 'keyword':keyWord}
                    if (dataIsNotBlocked(data)):                    
                        print(str(keyWord)+': '+str(title)+' '+str(url))
                        #data = archiveUrl(data)  #done in addNewsToCollection
                        if(addNewsToCollection(data)):
                            #mail
                            #time.sleep(random.uniform(160.5, 175.5))
                            foundNew = True
                            time.sleep(random.uniform(12.5, 14.55))
                            #time.sleep(10)
                            #sendNewsToMail(data) 
                        else:
                            time.sleep(17)
                storeCollection()
            else:
                print(response.text)   
                time.sleep(150) 
                #time.sleep(400) 
        if(not foundNew):
            print(["Nothing new", len(searchWords)])
        else:  
            print(["Found something", len(searchWords)])  
            searchWords.pop(keyWord, None)
        #foundZero    
