import os
from IRO import pbot, MONGO_DB_URI 
from telegram import * 
from pyrogram import Client , filters 
from pyrogram.types import Chat, Message, User 
from pymongo import MongoClient

levellink = [
    "https://telegra.ph/file/8a6319ed2e80c9e0ce4dc.mp4", 
    "https://telegra.ph/file/e162746b57234a0a65a26.mp4", 
    "https://telegra.ph/file/efddc21909ca5edff01ee.mp4", 
    "https://telegra.ph/file/d2c0b1e4e590f2c941b5c.mp4", 
    "https://telegra.ph/file/9feb100c211e1c3cd3c01.mp4", 
    "https://telegra.ph/file/8b9f7e314ab915eadb3ff.mp4", 
    "https://telegra.ph/file/dc99f2d3e1efad001d109.mp4", 
    "https://telegra.ph/file/24bd609d460cfbb4d29a9.mp4"
]

levelname = [
    "Team Rocket", "Stray God", "Vector", "Hero Association", 
    "Z Warrior", "Black Knight", "Ghoul", "Overlord"
]

levelnum = [2, 5, 15, 25, 35, 50, 70, 100]

MONGO_DB_URI = "mongodb+srv://ixbotmongodb:RadheRadhe@cluster0.ga1q2fn.mongodb.net/?retryWrites=true&w=majority"

def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in pgram.get_chat_members(chat_id, filter="administrators")
    ]

async def levelsystem(update: Update, context):
    leveldb = MongoClient(MONGO_DB_URI)
    toggle = leveldb["ToggleDb"]["Toggle"]
    if update.message.from_user:
        user = update.message.from_user.id
        chat_id = update.message.chat.id
        if user not in await is_admins(chat_id):
            return await update.message.reply_text("You are not admin")

    is_level = toggle.find_one({"chat_id": update.message.chat.id})
    if not is_level:
        toggle.insert_one({"chat_id": update.message.chat.id})
        await update.message.reply_text("Level System Enable")
    else:
        toggle.delete_one({"chat_id": update.message.chat.id})
        await update.message.reply_text("Level System Disable")

async def level(client, message):
    chat = message.chat.id
    user_id = message.from_user.id

    leveldb = MongoClient(MONGO_DB_URI)
    level = leveldb["LevelDb"]["Level"] 
    toggle = leveldb["ToggleDb"]["Toggle"]

    is_level = toggle.find_one({"chat_id": message.chat.id})
    if is_level:
        xpnum = level.find_one({"level": user_id, "chatid": chat})

        if not message.from_user.is_bot:
            if xpnum is None:
                newxp = {"level": user_id, "chatid": chat, "xp": 10}
                level.insert_one(newxp)
            else:
                xp = xpnum["xp"] + 10
                level.update_one({"level": user_id, "chatid": chat}, {"$set": {"xp": xp}})
                l = 0
                while True:
                    if xp < ((50*(l**2))+(50*(l))):
                        break
                    l += 1
                xp -= ((50*((l-1)**2))+(50*(l-1)))
                if xp == 0:
                    await message.reply_text(f"🌟 {message.from_user.mention}, You have reached level {l}**, Nothing can stop you on your way!")
                    for lv in range(min(len(levelname), len(levellink))):
                        if l == levelnum[lv]:            
                            Link = f"{levellink[lv]}"
                            await message.reply_video(video=Link, caption=f"{message.from_user.mention}, You have reached Rank Name {levelname[lv]}")

async def rank(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    
    
    leveldb = MongoClient(MONGO_DB_URI)
    level = leveldb["LevelDb"]["Level"] 
    toggle = leveldb["ToggleDb"]["Toggle"]
    is_level = toggle.find_one({"chat_id": message.chat.id})
    if is_level:
        xpnum = level.find_one({"level": user_id, "chatid": chat})
        xp = xpnum["xp"]
        l = 0
        r = 0
        while True:
            if xp < ((50*(l**2))+(50*(l))):
                break
            l += 1

        xp -= ((50*((l-1)**2))+(50*(l-1)))
        rank = level.find().sort("xp", -1)
        for k in rank:
            r += 1
            if xpnum["level"] == k["level"]:
                break                     
        await message.reply_text(f"{message.from_user.mention} Level Info:\nLevel: {l}\nProgess: {xp}/{int(200 *((1/2) * l))}\n Ranking: {r}")

application.add_handler(CommandHandler("level", levelsystem))
application.add_handler(MessageHandler(Filters.document | Filters.text | Filters.photo | Filters.sticker | Filters.animation | Filters.video, level))
application.add_handler(CommandHandler("rank", rank))

# Help message
__mod_name__ = "Rᴀɴᴋ"
__help__ = """
» /rank : ᴄʜᴇᴄᴋ ʏᴏᴜ ʀᴀɴᴋ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
» /level : ᴄʜᴇᴄᴋ ʏᴏᴜ ʟᴇᴠᴇʟ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
"""
