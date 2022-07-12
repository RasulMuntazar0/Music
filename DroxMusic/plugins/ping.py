import os

from telethon import Button, events

from DroxMusic import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/03b6a5f345ef6c1c9e6fb.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@DroxMusic"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@DroxMusic.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/DroxTeAm")]]
    await DroxMusic.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
