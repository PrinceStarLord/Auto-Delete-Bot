import os

API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

SESSION = os.getenv("SESSION", "")

TIME = int(os.getenv("TIME", 300)) #Delete time in seconds 

GROUPS = list(map(int, os.getenv("GROUPS", "").split())) 

ADMINS = list(map(int, os.getenv("ADMINS", "").split()))

START_MSG = "<b>Hello {},\n\nI'm a groups messages delete bot after a specific time.\n\nWorking for my owner groups.</b>"
