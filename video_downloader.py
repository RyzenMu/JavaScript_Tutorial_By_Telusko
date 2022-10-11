import requests
from bs4 import BeautifulSoup

yt_site = requests.get('https://www.youtube.com/watch?v=PlbupGCBV6w&list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4').text


soup = BeautifulSoup(yt_site, "lxml")

anchor_tags = soup.find("ytd-playlist-panel-video-renderer")

print(anchor_tags)