import requests
import json
import re

class snov:
    token=""
    access_id="57898884160e40c9b2e67bc653b7b643"
    access_secret="e232e1e0cf1717b452adc863b46b4584"
    def __init__(self):
        params = {
    'grant_type':'client_credentials',
    'client_id':self.access_id,
    'client_secret': self.access_secret
        }

        res = requests.post('https://app.snov.io/oauth/access_token', data=params)
        resText = res.text.encode('ascii','ignore')
        self.token=json.loads(resText)['access_token']
        #return json.loads(resText)['access_token']
    def get_email_count(self):
        #token = get_access_token()
        params = {'access_token':self.token,
                  'domain':'daralshifa.com'}
        res = requests.post('https://app.snov.io/restapi/get-domain-emails-count', data=params)
        return json.loads(res.text)
    def get_domain_search(self,domain):
        params = {'access_token':self.token,
                'domain':domain,
                'type': 'all',
                  'limit': 100
                }

        res = requests.post('https://app.snov.io/restapi/get-domain-emails-with-info', data=params)

        return re.findall(r'[\w\.-]+@[\w\.-]+',res)
# s=snov()
# #s.some()
# print((s.get_domain_search()))

