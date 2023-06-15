from ast import pattern
import requests
from bs4 import BeautifulSoup
import re

yt_site = requests.get('https://www.youtube.com/watch?v=PlbupGCBV6w&list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4').text


soup = BeautifulSoup(yt_site, "lxml")

# print(soup.prettify()) 

# pattern = 'https://\S+'

# pattern = 'Teluskoo'

# pattern = 'www.youtube.com/watch\S+'

# pattern = 'href="watch\S+'

# pattern = 'index\S+'

pattern = 'index\S+'

results = re.findall(pattern, str(soup.prettify()))

youtube_links = []
# regular expressions only works in string
#take out only the youtube links from script tag
for result in results:
    print()
    if '"webCommandMetadata":' in result:
        # print(str(result))
        print('------------------')
        print()
        pattern_inner = 'url\S+'
        link = re.findall(pattern_inner, str(result))
        print(link[0][6:85])
        full_link = 'https://www.youtube.com' + link[0][6:85]
        youtube_links.append(full_link)

        print('------------------')
        print()


from pytube import YouTube

# modifying the link to match the youtube link
# use full link starting from http to get the requests
for i, link in enumerate(youtube_links):
    modified_link = link[:44]
    my_video = YouTube(modified_link)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    print(modified_link)
    try:
        print(requests.get(modified_link), i)
    except:
        print('failed')

    








