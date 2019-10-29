import mechanize
from BeautifulSoup import BeautifulSoup as bs
import re
from snov import *
class validator:
    def __inti__(self,emails):
        chrome = mechanize.Browser()
        chrome.set_handle_robots(False)
        chrome.addheaders = [('User-agent', 
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
        base_url = 'https://www.google.co.in/search?q='
        test_file=emails
        valid=[]
        for i in test_file:
            i=i.strip()
            search_url = base_url +'"'+i.replace(' ', '+')+'"'
            htmltext = chrome.open(search_url).read()
            tag="<em>"+i+"</em>"
            l=len(re.findall(tag,htmltext))
            #print(l)
            if(l>0):
                print(i)
            valid.append(i)
        return valid