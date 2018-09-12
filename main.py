import requests
from daynamesources import day, because

state_identity = 'Plowface'
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdgCgjG50gWnO5DJbsyibTqNEKCcUeFRBCQbCKEpHp46mjVSw/formresponse'
payload = {'entry.522972278': state_identity,
           'entry.917801070': day(),
           'entry.1000005': because(),
           'draftResponse':[],
           'pageHistory':0}
user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSdgCgjG50gWnO5DJbsyibTqNEKCcUeFRBCQbCKEpHp46mjVSw/viewform','User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'}
r = requests.post(url, data=payload, headers=user_agent)
