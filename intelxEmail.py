import requests
import urllib3
import sys
urllib3.disable_warnings()

apikey='[intelx apikey here]'


seed = sys.argv[1]
headers = {
    'Host': '2.intelx.io',
    'Sec-Ch-Ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Origin': 'https://phonebook.cz',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

params1 = {
    'k': apikey,
}

data = '{"term":"' + seed + '","maxresults":10000,"media":0,"target":2,"terminate":[null],"timeout":20}'

response = requests.post('https://2.intelx.io/phonebook/search', params=params1, headers=headers, data=data, verify=False)
jsonResponse = response.json()
id = jsonResponse["id"]

params2 = {
    'k': apikey,
    'id': id,
    'limit': '10000',
}

response = requests.get('https://2.intelx.io/phonebook/search/result', params=params2, headers=headers, verify=False)
jsonResponse = response.json()
for i in range(len(jsonResponse["selectors"])):
	print(jsonResponse["selectors"][i]['selectorvalue'])



