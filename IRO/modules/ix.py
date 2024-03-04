"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits: 
    Void [https://github.com/Voidxtoxic/]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from IRO import UPDATES_CHANNEL, dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/faa3bfd69035c1c7b7341.jpg"


if UPDATES_CHANNEL == "Ix_updates":
    def void(update: Update, context: CallbackContext):

        TEXT = f"Wᴇʟᴄᴏᴍᴇ Tᴏ **[IX UPDATES](https://t.me/ix_updates)** \n\n◈ Ix ɪs ᴀɴ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ Cᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ sᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ. Gᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ Jᴏɪɴ ᴛʜᴇ Cᴏᴍᴍᴜɴɪᴛʏ ɪғ ɪᴛ ᴅʀᴀᴡs ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ."

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Aʙᴏᴜᴛ Ix", url="https://t.me/Ix_Updates/2"),
                    InlineKeyboardButton(text="Oᴡɴᴇʀ", url="https://t.me/bad_boy_og")
                    ],
                    [InlineKeyboardButton(text="Ix Uᴘᴅᴀᴛᴇs", url="https://t.me/Ix_Updates")]
                ]
            ),
        )


    ix_handler = CommandHandler("ix", ix, run_async = True)
    dispatcher.add_handler(void_handler)

    __help__ = """
    ──「Ix Uᴘᴅᴀᴛᴇs」──                         
    
    ❂ /ix : Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "Ix Uᴘᴅᴀᴛᴇs"
