import random

from telethon import Button
from IRO import dispatcher
from IRO import telethn as tbot
from IRO.events import register

PHOTO = [
    "https://graph.org/file/bbb62e54f12cd0a9818ab.jpg",
    "https://graph.org/file/bbb62e54f12cd0a9818ab.jpg",
]


@register(pattern=("/muichiro"))
async def awake(event):
    TEXT = f"Wᴇʟᴄᴏᴍᴇ Tᴏ **[𓆩『 ᴍᴜɪᴄʜɪʀᴏ ᴜᴘᴅᴀᴛᴇs 』𓆪](https://t.me/Muichiro_Updates)** \n\n ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀɴʏ ᴜᴘᴅᴀᴛᴇs ʀᴇɢᴀʀᴅɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ sᴏ ʏᴏᴜ ᴍᴜsᴛ Jᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ."
    BUTTON = [
        [
            Button.url("Oᴡɴᴇʀ​", f"https://t.me/Conc_chemical"),
            Button.url("Sᴜᴘᴘᴏʀᴛ​", f"https://t.me/Muichiro_support"),
            Button.url("Uᴘᴅᴀᴛᴇs​", f"https://t.me/Muichiro_Updates"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)

__mod_name__ = "Mᴜɪᴄʜɪʀᴏ Tᴏᴋɪᴛᴏ"
__help__ = """
 » /muichiro: ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ sʜᴏᴡ ʏᴏᴜ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ.
 """
