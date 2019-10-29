import whois
from snov import *
from validator import *


domain=input("Enter the input domain")
info = whois.query(domain)
whois_info=info.__dict__
for i,j in whois_info.items():
    print(i,j)
s=snov()
emails=s.get_domain_search(domain)
validator_object=validator(emails)
