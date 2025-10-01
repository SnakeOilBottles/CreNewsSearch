# newsapiLanguages =  ["ar","de","en","es","fr","he","it","nl","no","pt","ru","sw","ur","zh"]
# newsapiLanguages =  ["ar","de","en","es","fr","he","it","nl","no","pt","ru","sw","zh",   "el","ja"]

## DATA_PATH = Path.cwd()

class NewsBase:

    def __init__(self):
        ## ts = int(time.time())
        self.allLanguages = []
        return None

    def getServiceName(self):
        return 'unknown'
