import os
import asyncio
import filters
import html
from IRO import as pbot
from IRO.modules.helper_funcs.chat_status import (
    ADMIN_CACHE,
    bot_admin,
    can_pin,
    can_promote,
    connection_status,
    user_admin,
)

@pbot.on_message(filters.command("bots"))
async def listbots(client, message):
    try:
        botList = []
        async for bot in pbot.get_chat_members(
            message.chat.id, filter=enums.ChatMembersFilter.BOTS
        ):
            botList.append(bot.user)
        lenBotList = len(botList)
        text3 = f"**ʙᴏᴛ ʟɪsᴛ - {message.chat.title}**\n\n🤖 Bots\n"
        while len(botList) > 1:
            bot = botList.pop(0)
            text3 += f"├ @Dazai_ixbot\n"
        else:
            bot = botList.pop(0)
            text3 += f"└ @Dazai_ixbot\n\n"
            text3 += f"✅ | **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ ʙᴏᴛs**: {lenBotList}"
            await pbot.send_message(message.chat.id, text3)
    except FloodWait as e:
        await asyncio.sleep(e.value)
