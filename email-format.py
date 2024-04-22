import requests
from lxml import etree
from bs4 import BeautifulSoup
import urllib3
import sys
urllib3.disable_warnings()

seed = sys.argv[1]
headers = {
    'Host': 'www.email-format.com',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Sec-Ch-Ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

response = requests.get('https://www.email-format.com/d/'+seed+'/', headers=headers, verify=False)

soup = BeautifulSoup(response.content, "html.parser")
tree = etree.HTML(str(soup))

count = len(tree.xpath('//*[@id="domain_address_container"]/tbody/tr'))

for j in range(count):
    for i in tree.xpath('//*[@id="domain_address_container"]/tbody/tr['+str(j)+']/td/div[1]'):
        print(i.text.strip())

