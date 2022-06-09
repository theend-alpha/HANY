"""from HANY.AlphaDB.couples_adb import add_couple, c_is_selected, reset_couple, COUPLES
from pyrogram import filters, Client
import random
from datetime import datetime as dt 


a = dt.now()

if a.minute >= 30 and a.hour < 18:
	k = a.minute

	atime = str(a.hour + 6) + ":" + str(k - 30)


elif a.minute >= 30 and a.hour >= 18:
	k = a.minute
	t = a.hour
	
	atime = str(t - 18) + ":" + str(k - 30)
	
	
elif a.minute < 30 and a.hour < 19:
	k = a.minute
	t = a.hour
	
	atime = str(t + 5) + ":" + str(k + 30)

	
elif a.minute < 30 and a.hour >= 19:
	k = a.minute
	t = a.hour
	
	atime = str(t + 5 - 24) + ":" + str(k + 30)

reset_time = "0" + ":" + "0"

CHAT_LIST = []

@Client.on_message(filters.command("couple") & ~filters.edited)
async def couple(_, message):
    global CHAT_LIST
    if message.chat.type == "private":
	await message.reply_text("Try this command in groups")
	return
    try:
        async for i in _.iter_chat_members(message.chat.id):
	    if not i.user.is_bot:
	        CHAT_LIST.append(i.user.id)
	        c1_id = random.choice(CHAT_LIST)
		c2_id = random.choice(CHAT_LIST)
		while c1_id == c2_id:
		    c1_id = random.choice(CHAT_LIST)
		c1_mention = (await _.get_users(c1_id)).mention
	        c2_mention = (await _.get_users(c2_id)).mention
                """
