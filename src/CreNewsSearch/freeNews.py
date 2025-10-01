'''

af, ar, bg, bn, ca, cn, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr,
ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, tw, uk, ur, vi

'''

 # se not supported....
 # hi only without language
def inqRandomNews2():
    apiKey = os.getenv('FREENEWS_API_KEY')
    apiKey = '27df9d0a81msh4d292fffabdafdcp145cb9jsndf9f7c9c702e'  ## DELETE!

    #keyWord = random.choice(searchWords)
    #language = 'de'
    #language = 'en'   
    #language = 'fr' 
    keyWord = random.choice(list(searchWords.keys()))
    language = searchWords[keyWord]
    newLanguage = random.choice(newsapiLanguages)
    if((not newLanguage == language) & (random.uniform(0.0, 100.0)>60.0) & (not 'free' == language)):
        print('language: '+language+'; keyword: '+keyWord)
        keyWord = keyWord.strip("'")
        translatorList = []
        # if  GoogleTranslator.get_supported_languages(as_dict=True).values()
        translatorList.append(GoogleTranslator(source=language, target=newLanguage))
        translatorList.append(MyMemoryTranslator(source=language, target=newLanguage))   #-ud(ur?),se(sv?)
        if((not language in ['ar','he','no','se','ud','hi','sw','ur']) and (not newLanguage in ['ar','he','no','se','ud','hi','sw','ur'])):
            translatorList.append(LingueeTranslator(source=language, target=newLanguage))
        #Yandex, Deepl, QCRI needs API
        someTranslator = random.choice(translatorList)
        # keyWord = GoogleTranslator(source=language, target=newLanguage).translate(keyWord)
        try:
            newKeyWord = someTranslator.translate(keyWord)
            keyWord = "'" + newKeyWord + "'"
            language = newLanguage
        except deep_translator.exceptions.ElementNotFoundInGetRequest as e:
            print(['ElementNotFoundInGetRequest', e])
        except:
            print("Some exception in keyword translate - keep")
    lang2 = language
    if('zh'==language):
        lang2 = 'cn'
    if('ud'==language):
        lang2 = 'ur'
    # if('sv'==language):
    #     lang2 = 'sw'

    if(language in ['hi']):
        lang2 = 'free'

    if(not 'xx'==lang2):
        #searchWords.pop(keyWord)

        page = random.choice(['1','2','3','4','5'])  
        #page = '1'
        sort = random.choice(['relevancy', 'popularity', 'publishedAt'])
        #sort = 'relevancy'

        print('keyword: '+keyWord+'; Page: '+page)

        # https://free-docs.newscatcherapi.com/#request-parameters
        url = "https://free-news.p.rapidapi.com/v1/search"

        
        querystring = {"q":keyWord,"lang":lang2,"page":page,"page_size":"20"}
        if ('free' == lang2):
            querystring = {"q":keyWord,"page":page,"page_size":"20"}

        headers = {
            'x-rapidapi-key': apiKey,
            'x-rapidapi-host': "free-news.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        print(response.text)
        print(response.status_code)     #200
        foundNew = False
        foundZero = True
        if((response.text) and (not response.status_code in [204, 500, 504])):
            text = response.text
            #unless string: text = text.decode("utf-8")
            print(['string: ', isinstance(text,str)])
            if(not isinstance(text,str)):
                text = text.decode("utf-8")
            jsonData = json.loads(text)
            #print(jsonData)
            if (('ok'!=jsonData['status'])):
                    time.sleep(20) 
                    page = '1'
                    querystring = {"q":keyWord,"lang":lang2,"page":page,"page_size":"20"}
                    if ('free' == lang2):
                        querystring = {"q":keyWord,"page":page,"page_size":"20"}
                    response = requests.request("GET", url, headers=headers, params=querystring)
                    response.encoding = response.apparent_encoding
                    print(['string: ', isinstance(text,str)])
                    if(not isinstance(text,str)):
                        text = text.decode("utf-8")
                    jsonData = json.loads(response.text)   
                    #print(jsonData)
            if (('ok'==jsonData['status']) and (jsonData['total_hits']>0)):
                foundZero = False  
                for article in jsonData['articles']:
                    print(article)
                    title = article['title']
                    description = '' #  article['summary']
                    url = article['link']    # 'clean_url'
                    #later use list...
                    url = url.replace('https://www.zeit.de/zustimmung?url=', '')
                    url = url.replace('https://www.golem.de/sonstiges/zustimmung/auswahl.html?from=', '')
                    url = url.replace('%3A', ':')
                    url = url.replace('%2F', '/')                

                    domain = urlparse(url).netloc

                    data = extractInfo(url)
                    if('description' in data):
                        description = data['description']
                    else:
                        if(article['summary']):
                            description = article['summary'][0:500]   

                    image = article['media']
                    published = article['published_date']
                    # 'published_date': '2021-09-30 04:15:00', 'published_date_precision': 'full'


                    content = article['summary']
                    topic = article['topic']
                    country = article['country']
                    lang3 = article['language']
                    if(lang3):
                        if (lang2 == 'free'):
                            language = lang3
                            if('cn'==lang3):
                                language = 'zh'
                            #if('ur'==lang3):
                            #    language = 'ud'
                            if('sw'==lang3):
                                language = 'sv'
                            if('ca'==lang3):
                                language = 'fr'
                            if('af'==lang3):
                                language = 'en'                                                               

                    data = {'url':url, 'valid':0, 'domain':domain, 'en':'', 'published':published, 'description':description, 'title':title,
                           'image':image, 'content':content, 'language': language, 'keyword':keyWord, 'topic':topic, 'country':country}
                    if (dataIsNotBlocked(data)):                    
                        print(str(keyWord)+': '+str(title)+' '+str(url))
                        #data = archiveUrl(data)  #done in addNewsToCollection
                        if(addNewsToCollection(data)):
                            #mail
                            #time.sleep(random.uniform(160.5, 175.5))
                            foundNew = True
                            time.sleep(random.uniform(11.5, 14.55))
                            #time.sleep(10)
                            #sendNewsToMail(data) 
                        else:
                            time.sleep(35)
                storeCollection()
            else:
                print([language, lang2])
                print(response.text)   
                time.sleep(300) 
                #time.sleep(400) 
        if(not foundNew):
            print(["Nothing new", len(searchWords)])
        else:  
            print(["Found something", len(searchWords)])  
            #searchWords.pop(keyWord, None)
        #foundZero    
