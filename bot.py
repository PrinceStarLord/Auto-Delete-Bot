import os
import asyncio
from pyrogram import Client, filters, idle
from config import *

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )

Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
        if message.from_user.id in ADMINS:
            return
        else:
            await asyncio.sleep(TIME)
            await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
        print(f"Error occurred in delete function: {e}")

try:
    User.start()
    print("User Started!")
    Bot.start()
    print("Bot Started!")
    idle()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    User.stop()
    print("User Stopped!")
    Bot.stop()
    print("Bot Stopped!")
