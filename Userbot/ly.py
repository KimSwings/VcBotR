from pyrogram import Client, filters
from config import HNDLR, bot
import re
import requests
from PyLyrics import PyLyrics
r = requests.get('http://www.songlyrics.com/index.php?section=search&searchW=""&submit=Search')
k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)

@Client.on_message(filters.command(["lyrics", "l"], prefixes=f"{HNDLR}"))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics...")
pl=k[1]
x = requests.get(f'http://www.songlyrics.com/{pl}')
m = re.search(r'iComment-text">([^=]+)', x.text)
res = m[0].replace('<br />', '')
song = re.search(r'>([^<]+)', res) 
print(song[0])
query = message.text
if not query:
 await lel.edit("`What I am Supposed to find `")
return
)


   
