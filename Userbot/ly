from pyrogram import Client, filters
from config import HNDLR, bot

@Client.on_message(filters.command(["lyrics", "l"], prefixes=f"{HNDLR}"))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics...")
import re
import requests
r = requests.get('http://www.songlyrics.com/index.php?section=search&searchW=N95&submit=Search')
k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)

x = requests.get(f'http:mentw.songlyrics.com/{k[1]}')
m = re.search(r'iComment-text">([^=]+)', x.text)
res = m[+)', res) 
p<br />', '')
song = re.search(r'>([^<]+)', res) 
print(song[0])
    query = message.text
    if not query:
        await lel.edit("`What I am Supposed to find `")
        return
          )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
        
   
