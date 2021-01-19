import os
# import qrcode
import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, bot

# Enable logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# KKbot States

INPUT_TEXT = 0


# QR FUNTION ------------------------------------------------------------------
'''
def qr_command_handler(update, context):

    update.message.reply_text("Envieme el texto para generar un codigo QR:")

    return INPUT_TEXT


def generate_qr(text):

    filename = text + '.jpg'
    img = qrcode.make(text)

    print(filename)

    return ConversationHandler.END


def input_text(update, context):

    text = update.message.text
    print(text)

    filename = generate_qr(text)
    #send_qr(filename)

    return ConversationHandler.END
'''
# QR FUNTION ------------------------------------------------------------------

# KKbot Funtions

def help_command(update, context):
    update.message.reply_text("Commands:\n\n"
                              "/start - default action\n\n"
                              "/saluda - Saludo xd\n\n"
                              "/di - sEscriba /di + su mensaje para que el bot lo repita")


def start(update, context):

    update.message.reply_text("Iniciando modelo 0.01...")
    update.message.reply_text("Inicio Exitoso")
    update.message.reply_text("Hola soy Mr. KK, escribe /ayuda para leer sobre mis comandos")


def welcome(update, context):

    user = update.message.from_user

    update.message.reply_text("Bienvenid@ " .format(user['username'], user['id']))


def di(update, context: CallbackContext):

    msg = update.message.text

    update.message.reply_text(msg.strip('/di'))



if __name__ == '__main__':

    updater = Updater(token='1574460728:AAG5JdXQnh2S0VZ4tUQ8tLHxgcRrRnIDKi4', use_context=True)

    dp = updater.dispatcher

    # add handler
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('ayuda', help_command))

    dp.add_handler(CommandHandler('saluda', welcome))

    dp.add_handler(CommandHandler('di', di))

    # QR FUNTION ------------------------------------------------------------------
    '''
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))
    '''
    # QR FUNTION ------------------------------------------------------------------

    updater.start_polling()
    updater.idle()


