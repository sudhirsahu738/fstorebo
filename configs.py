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
💡 ** I am Telegram File Store Bot** 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [𝐊𝐗𝐓_𝐌𝐎𝐕𝐈𝐄𝐒](https://t.me/kxt_movies) 
│
├🔹👥 **Bot Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/kxt_movies)
│
├🔸🔔 **Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/kxt_movies)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@𝐊𝐗𝐓_𝐌𝐎𝐕𝐈𝐄𝐒](https://t.me/kxt_movies) 

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐢𝐬 𝐒𝐮𝐩𝐞𝐫 𝐍𝐨𝐨𝐛. 𝐉𝐮𝐬𝐭 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐟𝐫𝐨𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐃𝐨𝐜𝐬. 𝐀𝐧𝐝 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 𝐇𝐞𝐥𝐩 𝐅𝐫𝐨𝐦 𝐏𝐫𝐨 𝐂𝐨𝐝𝐞𝐫𝐬\n**@kxt_movies**

𝐈𝐟 𝐘𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐮𝐫 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤. 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫. 

𝐀𝐥𝐬𝐨 𝐫𝐞𝐦𝐞𝐦𝐛𝐞𝐫 𝐭𝐡𝐚𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐰𝐢𝐥𝐥 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐝𝐮𝐥𝐭 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐟𝐫𝐨𝐦 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐒𝐨 𝐛𝐞𝐭𝐭𝐞𝐫 𝐝𝐨𝐧'𝐭 𝐒𝐭𝐨𝐫𝐞 𝐓𝐡𝐨𝐬𝐞 𝐊𝐢𝐧𝐝 𝐨𝐟 𝐓𝐡𝐢𝐧𝐠𝐬.


"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n💡 ** I am aaTelegram File Store Bot**\n\n📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.\n\n❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
 """
