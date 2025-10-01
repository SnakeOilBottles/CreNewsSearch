import os
import sys
import math

import pandas as pd

from pathlib import Path
import os.path
import glob

import aiohttp
import asyncio
import io
import requests
from urllib.parse import urlparse
import json
import time
import smtplib
import random
import hashlib
import glob
from difflib import SequenceMatcher


## https://rapidapi.com/search/News%2C%20Media?sortBy=ByRelevance

# 
###
# https://rapidapi.com/rphrp1985/api/newsnow    50/m                 - only top news
# https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/bing-news-search1/pricing 1000/m    failed
# https://rapidapi.com/WorldNewsAPI/api/world-news3 50/d             - needs payment information
# https://rapidapi.com/opensorted/api/news-search9/pricing  300/m    - needs payment information
# https://rapidapi.com/ran-AlhXszqtp/api/news-api-lite/pricing 1000/m   ??failed??
# https://rapidapi.com/elterrien/api/search-news-feed 1000/h   failed
# https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/free-news   failed -> timeout!

#====================================================================+====
# 2024-12-19
# https://rapidapi.com/bonaipowered/api/google-news22       100/d    **!
# https://rapidapi.com/bonaipowered/api/news-api14          300/m    **!    (also gets Languages!)
# https://rapidapi.com/things4u-api4upro/api/google-news25  100/m    **!    (also gets Languages!)
# https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-news-data/  100/m  *!
# https://rapidapi.com/fxcoinapi/api/news-search4/pricing    50/m    **
# https://rapidapi.com/bilgisamapi-bilgisamapi-default       30/m    *
# https://rapidapi.com/bfd-id/api/google-news13/playground   25/m    *
# https://rapidapi.com/bilgisamapi-bilgisamapi-default/api/news-search-api-google-news-breaking-news 25/m *
# https://rapidapi.com/lafesummer/api/google-news-search     20/m    * 
# https://rapidapi.com/strataconsultingllc/api/newsapi90     20/m    *





################
import requests

url = "https://google-news25.p.rapidapi.com/search"

querystring = {"keyword":"facebook"}

headers = {
	"x-rapidapi-key": "27df9d0a81msh4d292fffabdafdcp145cb9jsndf9f7c9c702e",
	"x-rapidapi-host": "google-news25.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
##############



apiKey = '27df9d0a81msh4d292fffabdafdcp145cb9jsndf9f7c9c702e'  ## DELETE!
language = "de-DE"    ## 
country = "de" ##
keyWord = "Hochwasser"

category = 'CAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ'  # latest
category = 'CAQiRENCQVNMUW9JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURsdWJWOHFDUW9IRWdWWGIzSnNaQ2dBKioIAComCAoiIENCQVNFZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeWdBUAFQAQ'  ## world

url = "https://google-news25.p.rapidapi.com/search"
page = random.choice(['1','2','3','4','5'])  
querystring = {"keyword":keyWord,"language":language} # , "country":country
headers = {
    'x-rapidapi-key': apiKey,
    'x-rapidapi-host': "google-news25.p.rapidapi.com"
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
    print(jsonData)    # {'success': True, 'total': 0, 'data': []}


#{'status': 'error', 'error_code': 'WrongParameter', 'message': "[lang] parameter's form is not correct/not supported language"}

#504  {"messages":"The request to the API has timed out. Please try again later, or if the issue persists, please contact the API provider", "info": "Your Client (working) ---> Gateway (working) ---> API (took too long to respond)"}

#403  {"message":"You are not subscribed to this API."}
#400  {"success":false,"code":400,"message":"Bad Request","fields":[{"type":"querystring","name":"country","message":"Required"}]}


