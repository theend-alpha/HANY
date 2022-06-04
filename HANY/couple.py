""" from LifeGamesMain.AlphaDB.shipdb import get_couple, save_couple
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

COUPLE_LIST = []

CHAT_LIST = []

reset_time = "0" + ":" + "0"


while atime == reset_time:
	COUPLE_LIST.clear()


@Client.on_message(filters.command("couple") & ~filters.edited)
async def couple(_, message):
	if message.chat.type == "private":
	    await message.reply_text("Try this command in groups")
	    return
	
	try:
		chat_id = message.chat.id
		if len(COUPLE_LIST) == 0:
			for i in _.iter_chat_members(message.chat.id):
				if not i.user.is_bot:
					CHAT_LIST.append(i.user.id)
			c1_id = random.choice(CHAT_LIST)
			c2_id = random.choice(CHAT_LIST)
			while c1_id == c2_id:
				c1_id = random.choice(CHAT_LIST)
			c1_mention = (await _.get_users(c1_id)).mention
			c2_mention = (await _.get_users(c2_id)).mention
			c_s_m = OMFOO.format(c1_mention, c2_mention)
			
			await _.send_message(message.chat.id, c_s_m)
			COUPLE_LIST.append(c1_id)
			COUPLE_LIST.append(c2_id)
			
		elif len(COUPLE_LIST) == 2:
			c1_id = COUPLE_LIST[0]
			c2_id = COUPLE_LIST[1]
			c1_mention = (await _.get_users(c1_id)).mention
			c2_mention = (await _.get_users(c2_id)).mention
			c_s_m = OMFOO.format(c1_mention, c2_mention)
			
			await _.send_message(message.chat.id, c_s_m) 	 
	except Exception as e:
		await message.reply_text(f"Error : {e}") """
