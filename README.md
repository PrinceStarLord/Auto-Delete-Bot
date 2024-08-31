<p align="center">
𝗔𝗨𝗧𝗢-𝗗𝗘𝗟𝗘𝗧𝗘-𝗕𝗢𝗧
</p>

## Variables
1. `API_ID` : Get from [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your telegram bot token from [@BotFather](https://t.me/BotFather)
4. `SESSION` : Generate from here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://repl.it/@subinps/getStringName)
5. `GROUPS` : ID of Groups (seperate by spaces)
6. `ADMINS` : ID of Admins, messages from admins will not delete (seperate by spaces)
7. `TIME` : Time in seconds

## Example variables

```sh
API_ID = int(os.getenv("API_ID", "1234"))
API_HASH = os.getenv("API_HASH", "tud737bxha")
BOT_TOKEN = os.getenv("BOT_TOKEN", "1836482342:tdabfnehjsbhcb")
SESSION = os.getenv("SESSION", "iuwfggvsafkewfdwfisfh")
TIME = int(os.getenv("TIME", 300)) 
GROUPS = list(map(int, os.getenv("GROUPS", "-1005787482627").split())) 
ADMINS = list(map(int, os.getenv("ADMINS", "8397461824 6482361944").split()))
```

### Make sure:
- Fill up [config.py](https://github.com/PrinceStarLord/Auto-Delete-Bot/blob/main/config.py) properly, all variables are required.
- Add Bot as admin in Groups with delete permission
- Join groups from user account & add admin with delete permission

## Deploy in your VPS

```sh
git clone https://github.com/PrinceStarLord/Auto-Delete-Bot
cd Auto-Delete-Bot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

### Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
