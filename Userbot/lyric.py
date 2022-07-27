import re
import requests
r = requests.get('http://www.songlyrics.com/index.php?section=search&searchW=darling+nikki&submit=Search')
k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)

x = requests.get(f'http://www.songlyrics.com/{k[1]}')
m = re.search(r'iComment-text">([^=]+)', x.text)
res = m[0].replace('<br />', '')
song = re.search(r'>([^<]+)', res) 
print(song[0])
