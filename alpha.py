import config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":EndAfkBot:",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="EndAfk"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid,Fooling Alpha or what !")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid,Bot token Bruhh!")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully visit other repositories of Alpha!")
    idle()
    app.stop()
    print("Bot stopped. problem is yours coz this repo made by alpha !")
