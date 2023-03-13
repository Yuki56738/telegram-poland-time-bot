#!/usr/bin/env python3

import datetime
import re

import telegram.ext
from telegram.ext import Updater
from telegram.ext import *
from telegram import *
import logging
from datetime import *
import os
import deepl
from deepl import *

DEEPL_API_KEY="7cdb289f-f521-70ca-e880-9725c281584f:fx"
TOKEN = "5479025637:AAFun8ISKZsnCnnmqtRiN7hmOcLgTIki8F0"
# from telegram.ext import Application

"""
Done! Congratulations on your new bot. You will find it at t.me/Yuki_s_first_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

"""

# updater = Updater(token="5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo")

# dispatcher = updater.dispatcher

# def start(bot: ExtBot, update: Updater):
transletor = deepl.Translator(DEEPL_API_KEY)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes) -> None:
    user = update.effective_user
    await update.message.reply_html(rf"Hi {user.mention_html()}! Type sentence to translate!", reply_markup=ForceReply(selective=True))
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    msg = update.message.text
    # msg2 = context.args
    result = transletor.translate_text(msg, target_lang="EN-US")
    result2 = transletor.translate_text(msg, target_lang="JA")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{result.text}\n{result2.text}")
async def ping(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Pong!")
    print(update.effective_chat.id)
async def poland(update: Update, ctx:ContextTypes.DEFAULT_TYPE):
    # dtNow = datetime.now(timedelta=timedelta(hours=1))
    # dtNow = datetime.now(tz=timezone.utc)
    # tz_poland = timezone(timedelta(hours=7), name="poland")

    # dtPoland = datetime.now(tz=tz_poland)
    # dtNowPoland2 = datetime.now(tz=timezone("poland"))
    dtNowPoland = datetime.now(timezone(timedelta(hours=2)))
    await ctx.bot.send_message(chat_id=update.effective_chat.id, text=str(dtNowPoland))
async def japan(update: Update, ctx:ContextTypes.DEFAULT_TYPE):
    dtNowJapan = datetime.now(timezone(timedelta(hours=9)))
    await ctx.bot.send_message(chat_id=update.effective_chat.id, text=str(dtNowJapan))
async def trans(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    msg = re.sub("/trans", "", msg)
    result = transletor.translate_text(msg, target_lang="EN-US")
    result2 = transletor.translate_text(msg, target_lang="JA")
    await ctx.bot.send_message(chat_id=update.effective_chat.id, text=f"{result}\n{result2}")
if __name__ == '__main__':
    # application = Bot(token="5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo")
    app = Application.builder().token(TOKEN).build()
    # app = ApplicationBuilder().token("5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo").build()
    # updater = Updater(TOKEN)
    # dp:Application = updater.dispatcher
    start_handler = CommandHandler('trans', trans)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    ptime_handler = CommandHandler('poland', poland)
    ping_handler = CommandHandler('ping',ping)
    japan_handler = CommandHandler('japan', japan)
    # message_handler = MessageHandler()
    # trans_handler = CommandHandler('trans', trans)
    app.add_handler(start_handler)
    # app.add_handler(echo_handler)
    app.add_handler(ping_handler)
    app.add_handler(ptime_handler)
    app.add_handler(japan_handler)
    # app.add_handler(trans_handler)
    # app.run_polling()
    PORT = int(os.environ.get("PORT", "8443"))
    # app.bot.send_message(chat_id=1486744027, text="Hello.")
    # app.bot.setWebhook(url="")

    app.run_polling()

    # updater.start_polling()
    # updater.start_webhook(
    #     listen="0.0.0.0",
    #     port=int(PORT),
    #     url_path=TOKEN,
    #     webhook_url="https://telegram-webhook-yuki.herokuapp.com/" + TOKEN
    # )
    # app.run_webhook(
    #     listen="0.0.0.0",
    #     port=PORT,
    #     url_path=TOKEN,
    #     webhook_url="https://tele-yuki.herokuapp.com/" + TOKEN
    # )
