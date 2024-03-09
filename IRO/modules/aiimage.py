from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.enums import ChatAction
from pyrogram.types import InputMediaPhoto
from .. import pbot as  IRO,BOT_USERNAME
import requests

@IRO.on_message(filters.command("imagine"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "`» ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...,\n\n» ɢᴇɴᴇʀᴀᴛɪɴɢ ᴘʀᴏᴍᴘᴛ .. ...`")
    results= requests.get(f"https://iro-api.vercel.app/imagine/{text}").json()["results"]

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ 

» ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ➛ [𝗗𝗔𝗭𝗔𝗜](https://t.me/Dazai_ixbot)
» ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➛ {message.from_user.mention}
"""
    await m.delete()
    photos=[]
    for i in range(5):
        photos.append(InputMediaPhoto(results[i]))
    photos.append(InputMediaPhoto(results[5], caption=caption))
    await b.send_media_group(message.chat.id, media=photos)
    
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
__mod_name__ = "Aɪ-Iᴍᴀɢᴇ"
__help__ = """
 » /imagine ➛ ɢᴇɴᴇʀᴀᴛᴇ ᴀɪ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ
 » /mahadev ➛ ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
 """
