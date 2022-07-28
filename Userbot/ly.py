import re

from ..func import http
from telethon import events
from ubb import Ubot
from pyrogram import Client, filters

@Client.on_message(filters.command(["lyrics", "l"], prefixes=f"{HNDLR}"))
async def songlyric(event):
    query = event.message.message[len('.lyrics '):]
    Query = query.replace(' ', '+')
    try:
        r = await http.get(f'http://www.songlyrics.com/index.php?'+
                           f'section=search&searchW={Query}&submit=Search')
        k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)
        if 'did not match any results' in r.text:
            return await event.edit("**Not Found**")

        x = await http.get(f'http://www.songlyrics.com/{k[1]}')
        m = re.search(r'iComment-text">([^=]+)', x.text)
        res = m[0].replace('<br />', '')
        output = re.search(r'>([^<]+)', res)
        await event.edit(f'**Input**: `{query}`\n`{output[0]}`')
    except:
        await event.edit('Failed error')
