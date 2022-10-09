#!/usr/bin/env python3

import datetime

import telegram.ext
from telegram.ext import Updater
from telegram.ext import *
from telegram import *
import logging
from datetime import *
import os

TOKEN = "5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo"
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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes) -> None:
    user = update.effective_user
    await update.message.reply_html(rf"Hi {user.mention_html()}!", reply_markup=ForceReply(selective=True))
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
async def ping(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Pong!")
async def poland(update: Update, ctx:ContextTypes.DEFAULT_TYPE):
    # dtNow = datetime.now(timedelta=timedelta(hours=1))
    dtNow = datetime.now(tz=timezone.utc)
    tz_poland = timezone(timedelta(hours=7), name="poland")
    # dtPoland = datetime.now(tz=tz_poland)
    dtNowPoland = datetime.now(timezone(timedelta(hours=2)))
    await ctx.bot.send_message(chat_id=update.effective_chat.id, text=str(dtNowPoland))
async def japan(update: Update, ctx:ContextTypes.DEFAULT_TYPE):
    dtNowJapan = datetime.now(timezone(timedelta(hours=9)))
    await ctx.bot.send_message(chat_id=update.effective_chat.id, text=str(dtNowJapan))
if __name__ == '__main__':
    # application = Bot(token="5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo")
    # application = Application.builder().token("TOKEN").build()
    app = ApplicationBuilder().token("5479025637:AAHky8UZoT9EKrv5lRLELqjI-qs__ZsPxpo").build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    ptime_handler = CommandHandler('poland', poland)
    ping_handler = CommandHandler('ping',ping)
    japan_handler = CommandHandler('japan', japan)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler(ping_handler)
    app.add_handler(ptime_handler)
    app.add_handler(japan_handler)
    # app.run_polling()
    PORT = int(os.environ.get("PORT", "8443"))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url="https://telegram-webhook-yuki.herokuapp.com/" + TOKEN
    )
