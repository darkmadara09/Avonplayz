import asyncio
import datetime
import re
from datetime import datetime
import os
import psutil
import time

from telethon import custom, events

from IRO import telethn as bot,BOT_NAME
from IRO import telethn as tgbot
from IRO.events import register 
import IRO.modules.sql.users_sql as sql
from IRO import StartTime
import IRO.utils.formatter as formatter


edit_time = 5
f""" ======================={BOT_NAME}====================== """
file1 = "https://telegra.ph/file/9a85d0a873e2dd80d278d.jpg"
file2 = "https://telegra.ph/file/9e7815284031452afa9e5.jpg"
file3 = "https://telegra.ph/file/dcc5e003287f69acea368.jpg"
file4 = "https://telegra.ph/file/ed1ce7fee94f46b0f671e.jpg"
file5 = "https://telegra.ph/file/701028ce085ecfa961a36.jpg"
""" ======================={BOT_NAME}====================== """


@register(pattern="/mbbbjyinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", data="statsinfo")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ {firstname}, \nᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ \n ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statsinfo")))
async def callback_query_handler(event):
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    users = sql.num_users()
    chats = sql.num_chats()
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "➤ Dᴀᴢᴀɪ Cᴜʀʀᴇɴᴛ Sʏsᴛᴇᴍ Sᴛᴀᴛs \n\n"
        LILIE += f"────────────────────────\n"
        LILIE += f"• UPTIME: {formatter.get_readable_time((bot_uptime))}\n"
        LILIE += f"• BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB \n"
        LILIE += f"• CPU: {cpu}% \n"
        LILIE += f"• RAM: {mem}%\n"
        LILIE += f"• DISK: {disk}%\n"
        LILIE += f"• CHATS: {chats}\n"
        LILIE += f"• USERS: {users}\n"
        LILIE += f"────────────────────────\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
