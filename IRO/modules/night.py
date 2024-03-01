from telethon import Button

from IRO import telethn
from IRO.events import register

PHOTO = "https://telegra.ph/file/8033a31e655db5312e40b.mp4"


@register(pattern=("Good night"))
async def awake(event):
    NEKO = f"❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❀\n\n✦ ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {event.sender.first_name}\n\n✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [𝗗𝗔𝗭𝗔𝗜](https://t.me/Dazai_ixbot)"
    BUTTON = [
        [
            Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Ix_Updates"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
