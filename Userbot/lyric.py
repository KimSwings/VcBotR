from pyrogram import Client, filters
import re
import requests
r = requests.get('http://www.songlyrics.com/index.php?section=search&searchW=darling+nikki&submit=Search')
k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)

from pyrogram import Client as pbot
@Client.on_message(filters.command(["lyrics", "l"], prefixes=f"{HNDLR}"))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics...")
    
    x = requests.get(f'http://www.songlyrics.com/{k[1]}')
m = re.search(r'iComment-text">([^=]+)', "x.text")
res = m[0].replace('<br />', '')
song = re.search(r'>([^<]+)', res) 
print(song[0])
