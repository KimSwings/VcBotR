@Client.on_message(filters.command(["del"], prefixes=f"{HNDLR}"))
@authorised_users_only
async def ping(client, m: Message):
 replied = m.reply_to_message
    #chat_id = m.chat.id
    #m.chat.title
    if replied:
        if replied.audio or replied.voice:
            await m.delete()
