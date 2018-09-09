import requests, daynamesources

url = 'https://docs.google.com/forms/d/e/1FAIpQLScC1fY4nkNKuX8co7ivxEoT0XGX4Yz_T5UIrTruvOk7Aqa8MA/formResponse'

payload = {'entry.895362114':'Plowman',
           'entry.346635073':'RESPONSEO',
           'entry.49460226':'Another dope mane',
           'draftResponse':[],
           'pageHistory':0}

user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLScC1fY4nkNKuX8co7ivxEoT0XGX4Yz_T5UIrTruvOk7Aqa8MA/viewform','User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'}

r = requests.post(url, data=payload, headers=user_agent)
