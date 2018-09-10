import random, json, re, requests, random

app_id = '96d58ebb'
app_key = '0dd1b3c11be7595c17e5dba593dbf36c'
# api_url_base = 'https://od-api.oxforddictionaries.com/api/v1'

wordlist_url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/en/domains=Art'

day_request = requests.get(wordlist_url, headers = {'app_id': app_id, 'app_key': app_key})
words = day_request.json()

words['results'][0]['word']

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|\n')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def day():
    new_day = 'test'
    return new_day

def because():
    get_quote = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&').json()
    new_reason = cleanhtml(new_reason[0]['content'])
    return new_reason
