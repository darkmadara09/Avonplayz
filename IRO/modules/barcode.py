from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.enums import ChatAction

from .. import pbot as  IRO,BOT_USERNAME
import requests


@IRO.on_message(filters.command("qrcode"))
async def qrcode_(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "» `ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...,\n\n❍ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ǫʀᴄᴏᴅᴇ ...`")
    write = requests.get(f"https://iro-api.vercel.app/qrcode/{text}").json()["results"]

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ǫʀᴄᴏᴅᴇ 

» **ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ➛** @{BOT_USERNAME}
» **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➛** {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
__mod_name__ = "ǫʀᴄᴏᴅᴇ"
__help__ = """
 ❍ /qrcode ➛ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ǫʀᴄᴏᴅᴇ
 """
