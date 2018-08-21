#!/usr/bin/python3

import random, requests, json

app_id = '96d58ebb'
app_key = '0dd1b3c11be7595c17e5dba593dbf36c'
api_url_base = 'https://od-api.oxforddictionaries.com/api/v1'
language = 'en'

wordlist_url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/registers=Rare;domains=Art'
domains_url = 'https://od-api.oxforddictionaries.com:443/api/v1/domains/' + language

req = requests.get(wordlist_url, headers = {'app_id': app_id, 'app_key': app_key})
domains = requests.get(domains_url, headers = {'app_id': app_id, 'app_key': app_key})

print(req.text)
print("Here's the domain list\n")
print(json.dumps(domains.json()))



# def new_word():
    
