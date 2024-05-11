"""
Prints telegram session string key
"""

from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = str(input("Input telegram API_ID: "))
API_HASH = str(input("Input telegram API_HASH: "))

with TelegramClient(
    session=StringSession(), api_id=API_ID, api_hash=API_HASH
) as client:
    print("Session string: ", client.session.save())