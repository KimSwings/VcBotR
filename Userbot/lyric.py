import re
import requests
r = requests.get('http://www.songlyrics.com/index.php?section=search&searchW=darling+nikki&submit=Search')
k = re.findall(r'href="http://www.songlyrics.com/([^"]+)', r.text)
import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot
@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics...")
    query = message.text
    x = requests.get(f'http://www.songlyrics.com/{k[1]}')
m = re.search(r'iComment-text">([^=]+)', x.text)
res = m[0].replace('<br />', '')
song = re.search(r'>([^<]+)', res) 
print(song[0])

    if not query:
        await lel.edit("`What I am Supposed to find `")
        return
        
    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try fumking off`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try just fumk off"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
