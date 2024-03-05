import random

from telethon import Button
from IRO import dispatcher
from IRO import telethn as tbot
from IRO.events import register

PHOTO = [
    "https://telegra.ph/file/293a1b0ffe0c24dfc2af3.jpg",
    "https://telegra.ph/file/293a1b0ffe0c24dfc2af3.jpg",
]


@register(pattern=("/ix"))
async def awake(event):
    TEXT = f"Wᴇʟᴄᴏᴍᴇ Tᴏ **[𝖨𝖷 𝖴𝖯𝖣𝖠𝖳𝖤𝖲](https://t.me/ix_updates)** \n\n Ix ɪs ᴀɴ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ Cᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ sᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ. Gᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ Jᴏɪɴ ᴛʜᴇ Cᴏᴍᴍᴜɴɪᴛʏ ɪғ ɪᴛ ᴅʀᴀᴡs ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ."
    BUTTON = [
        [
            Button.url("Oᴡɴᴇʀ​", f"https://t.me/Bad_Boy_Og"),
            Button.url("Sᴜᴘᴘᴏʀᴛ​", f"https://t.me/Ixsupport"),
        ]
        [
            Button.url("Uᴘᴅᴀᴛᴇs​", f"https://t.me/Ix_updates"),
    
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Ix"
