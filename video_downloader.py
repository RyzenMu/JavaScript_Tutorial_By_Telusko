from ast import pattern
import requests
from bs4 import BeautifulSoup
import re

yt_site = requests.get('https://www.youtube.com/watch?v=PlbupGCBV6w&list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4').text


soup = BeautifulSoup(yt_site, "lxml")

# print(soup.prettify()) 

# pattern = 'https://\S+'

# pattern = 'Telusko'

# pattern = 'www.youtube.com/watch\S+'

# pattern = 'href="watch\S+'

# pattern = 'index\S+'

pattern = 'index\S+'

results = re.findall(pattern, str(soup.prettify()))


for result in results:
    print()
    if '"webCommandMetadata":' in result:
        # print(str(result))
        print('------------------')
        print()
        pattern_inner = 'url\S+'
        link = re.findall(pattern_inner, str(result))
        print(link[0][6:84])
        print('------------------')
        print()
