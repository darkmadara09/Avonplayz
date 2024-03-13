import html
import re

from telegram import ParseMode
from telegram.ext import ChatJoinRequestHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.update import Update
from telegram.utils.helpers import mention_html

from IRO import dispatcher
from IRO.modules.helper_funcs.chat_status import bot_admin, user_can_restrict_no_reply
from IRO.modules.helper_funcs.decorators import Exoncallback
from IRO.modules.log_channel import loggable


def chat_join_req(upd: Update, ctx: CallbackContext):
    bot = ctx.bot
    user = upd.chat_join_request.from_user
    chat = upd.chat_join_request.chat
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ᴀᴘᴘʀᴏᴠᴇ", callback_data="cb_approve={}".format(user.id)
                ),
                InlineKeyboardButton(
                    "ᴅᴇᴄʟɪɴᴇ", callback_data="cb_decline={}".format(user.id)
                ),
            ]
        ]
    )
    bot.send_message(
        chat.id,
        "{} ᴡᴀɴᴛs ᴛᴏ ᴊᴏɪɴ {}".format(
            mention_html(user.id, user.first_name), chat.title or "this chat"
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


@IROcallback(pattern=r"cb_approve=")
@user_can_restrict_no_reply
@bot_admin
@loggable
def approve_joinreq(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    user = update.effective_user
    chat = update.effective_chat
    match = re.match(r"cb_approve=(.+)", query.data)

    user_id = match.group(1)
    try:
        bot.approve_chat_join_request(chat.id, user_id)
        update.effective_message.edit_text(
            f"ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {mention_html(user.id, user.first_name)}.",
            parse_mode="HTML",
        )
        logmsg = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#𝐉𝐎𝐈𝐍_𝐑𝐄𝐐𝐔𝐄𝐒𝐓\n"
            f"ᴀᴘᴘʀᴏᴠᴇᴅ\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>ᴜsᴇʀ:</b> {mention_html(user_id, html.escape(user.first_name))}\n"
        )
        return logmsg
    except Exception as e:
        update.effective_message.edit_text(str(e))


@IROcallback(pattern=r"cb_decline=")
@user_can_restrict_no_reply
@bot_admin
@loggable
def decline_joinreq(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    user = update.effective_user
    chat = update.effective_chat
    match = re.match(r"cb_decline=(.+)", query.data)

    user_id = match.group(1)
    try:
        bot.decline_chat_join_request(chat.id, user_id)
        update.effective_message.edit_text(
            f"ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ᴅᴇᴄʟɪɴᴇᴅ ʙʏ {mention_html(user.id, user.first_name)}.",
            parse_mode="HTML",
        )
        logmsg = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#𝐉𝐎𝐈𝐍_𝐑𝐄𝐐𝐔𝐄𝐒𝐓\n"
            f"ᴅᴇᴄʟɪɴᴇᴅ\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>ᴜsᴇʀ:</b> {mention_html(user_id, html.escape(user.first_name))}\n"
        )
        return logmsg
    except Exception as e:
        update.effective_message.edit_text(str(e))


dispatcher.add_handler(ChatJoinRequestHandler(callback=chat_join_req, run_async=True))
