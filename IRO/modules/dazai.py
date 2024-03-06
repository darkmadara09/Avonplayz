import random
from IRO.events import register
from IRO import telethn

APAKAH_STRING = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


@register(pattern="^/dazai ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("I ʜᴀᴠᴇ ɴᴏ ᴅᴇsɪʀᴇ ғᴏʀ ᴏᴛʜᴇʀs ᴛᴏ ᴛᴀᴋᴇ ɪᴛ ᴏɴ ᴛʜᴇᴍsᴇʟᴠᴇs ᴛᴏ ᴀɴᴀʟʏᴢᴇ ᴍʏ ᴛʜᴏᴜɢʜᴛs. I ᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴛʜᴏᴜɢʜᴛs.")
        return
    await event.reply(random.choice(APAKAH_STRING))

__mod_name__ = "Dᴀᴢᴀɪ"
__help__ = """
 ❍ /dazai ➛ sᴘᴇᴄɪᴀʟ ᴄᴏᴍᴍᴀɴᴅ.
 """
