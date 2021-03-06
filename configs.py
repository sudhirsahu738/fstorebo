# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
ð¡ ** I am Telegram File Store Bot** 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

â­ââââ[ **ðFÉªÊá´Sá´á´Êá´Bá´á´ð**]âââââ
â
âð¸ð¤ **My Name:** [ðð¢ð¥ð ðð­ð¨ð«ð ðð¨ð­](https://t.me/{BOT_USERNAME})
â
âð¸ð **Language:** [ðð²ð­ð¡ð¨ð§ð](https://www.python.org)
â
âð¹ð **Library:** [ðð²ð«ð¨ð ð«ðð¦](https://docs.pyrogram.org)
â
âð¹ð¡ **Hosted On:** [ððð«ð¨ð¤ð®](https://heroku.com)
â
âð¸ð¨âð» **Developer:** [ððð_ðððððð](https://t.me/kxt_movies) 
â
âð¹ð¥ **Bot Support:** [ðð®ð©ð©ð¨ð«ð­](https://t.me/kxt_movies)
â
âð¸ð **Bot Updates:** [ðð©ððð­ðð¬](https://t.me/kxt_movies)
â
â°ââââââ[ ð ]ââââââââââââ
"""
	ABOUT_DEV_TEXT = f"""
ð§ð»âð» **ðð²ðð²ð¹ð¼ð½ð²ð¿:** [@ððð_ðððððð](https://t.me/kxt_movies) 

ððð¯ðð¥ð¨ð©ðð« ð¢ð¬ ðð®ð©ðð« ðð¨ð¨ð. ðð®ð¬ð­ ðððð«ð§ð¢ð§ð  ðð«ð¨ð¦ ðððð¢ðð¢ðð¥ ðð¨ðð¬. ðð§ð ðððð¤ð¢ð§ð  ððð¥ð© ðð«ð¨ð¦ ðð«ð¨ ðð¨ððð«ð¬\n**@kxt_movies**

ðð ðð¨ð® ð°ðð§ð­ ð­ð¨ ðð¨ð§ðð­ð ðð®ð« ððð«ð ðð¨ð«ð¤. ðð¨ð® ððð§ ðð¨ð§ð­ððð­ ðð¡ð ððð¯ðð¥ð¨ð©ðð«. 

ðð¥ð¬ð¨ ð«ðð¦ðð¦ððð« ð­ð¡ðð­ ððð¯ðð¥ð¨ð©ðð« ð°ð¢ð¥ð¥ ððð¥ðð­ð ððð®ð¥ð­ ðð¨ð§ð­ðð§ð­ð¬ ðð«ð¨ð¦ ððð­ðððð¬ð. ðð¨ ððð­ð­ðð« ðð¨ð§'ð­ ðð­ð¨ð«ð ðð¡ð¨ð¬ð ðð¢ð§ð ð¨ð ðð¡ð¢ð§ð ð¬.


"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nð¡ ** I am aaTelegram File Store Bot**\n\nð¢ Send me any File & It will be uploaded in My Database & You will Get the File Link.\n\nâ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
 """
