from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text("🚀 Bot Revolusi Crypto Rindra Aktif!")

updater = Updater(BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
