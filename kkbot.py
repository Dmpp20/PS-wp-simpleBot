import os
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):

    update.message.reply_text("Buenas")


if __name__ == '__main__':

    updater = Updater(token='1574460728:AAG5JdXQnh2S0VZ4tUQ8tLHxgcRrRnIDKi4', use_context=True)

    dp = updater.dispatcher

    # add handler
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


