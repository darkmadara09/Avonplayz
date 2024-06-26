import os

from IRO import pbot, MONGO_DB_URI
from telegram import *
from pyrogram import Client , filters
from pyrogram.types import Chat, Message, User
from pymongo import MongoClient


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in pbot.get_chat_members(
            chat_id, filter="administrators"
        )
    ]

levellink =["https://telegra.ph/file/8a6319ed2e80c9e0ce4dc.mp4", "https://telegra.ph/file/e162746b57234a0a65a26.mp4", "https://telegra.ph/file/efddc21909ca5edff01ee.mp4", "https://telegra.ph/file/d2c0b1e4e590f2c941b5c.mp4", "https://telegra.ph/file/9feb100c211e1c3cd3c01.mp4", "https://telegra.ph/file/8b9f7e314ab915eadb3ff.mp4", "https://telegra.ph/file/dc99f2d3e1efad001d109.mp4", "https://telegra.ph/file/24bd609d460cfbb4d29a9.mp4"]
levelname = ["Team Rocket", "Stray God", "Vector", "Hero Association", "Z Warrior", "Black Knight", "Ghoul", "Overlord"]
levelnum = [2,5,15,25,35,50,70,100]



@pbot.on_message(
    filters.command("level", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def levelsystem(_, message): 
    leveldb = MongoClient(MONGO_DB_URI)
   
    toggle = leveldb["ToggleDb"]["Toggle"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_level = toggle.find_one({"chat_id": message.chat.id})
    if not is_level:
        toggle.insert_one({"chat_id": message.chat.id})
        await update.effective_message.reply_text("Level System Enable")
    else:
        toggle.delete_one({"chat_id": message.chat.id})
        await update.effective_message.reply_text("Level System Disable")


@pbot.on_message(
    (filters.document
     | filters.text    | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & ~filters.private,
    group=8,
)
async def level(client: Client, message: Message):
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
                level.update_one({"level": user_id, "chatid": chat}, {
                    "$set": {"xp": xp}})
                l = 0
                while True:
                    if xp < ((50*(l**2))+(50*(l))):
                         break
                    l += 1
                xp -= ((50*((l-1)**2))+(50*(l-1)))
                if xp == 0:
                    await message.reply_text(f"🌟 {message.from_user.mention}, You have reached level {l}**, Nothing can stop you on your way!")
    
                    for lv in range(len(levelname)) and range(len(levellink)):
                            if l == levelnum[lv]:            
                                Link = f"{levellink[lv]}"
                                await message.reply_video(video=Link, caption=f"{message.from_user.mention}, You have reached Rank Name **{levelname[lv]}**")
                  

                               
@pbot.on_message(
    filters.command("rank", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rank(client: Client, message: Message):
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
