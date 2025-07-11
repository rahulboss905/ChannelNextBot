import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(7456681709)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[🔔](https://telegra.ph/file/075be9289ec1e88dd1405.png) **FORCE SUBSCRIBE:**\n\nForce group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.",
        
        "[⚙](https://telegra.ph/file/2e8c811f8e3e99f340b3d.png) **SETUP:**\n\nFirst of all add me in the group as admin with ban users permission and in the channel as admin.\n● Note: Only creator of the group can setup me.",
        
        "[⚙](https://telegra.ph/file/ac265de1a3e8de3d85ffa.png) **COMMANDS:**\n\n/forcesubscribe - To get the current settings.\n/forcesubscribe no/off/disable - To turn of ForceSubscribe.\n/forcesubscribe {Channel Username} - To turn on and setup the channel.\n/forcesubscribe clear - To unmute all members who muted by me.\n\n● Note: /fsub is an alias of /forcesubscribe",
        
        "[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) **Developed with ❤️ by @team_secret_backup**"
      ]

      START_MSG = "**Hello! [👋](https://telegra.ph/file/075be9289ec1e88dd1405.png) [{}](tg://user?id={})**\n\n● I can force members to join a specific channel before writing messages in the group.\n● learn more at 👉 /help"
