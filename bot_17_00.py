#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# ```222
#-------laska
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    kb = [[InlineKeyboardButton("Кафедра КМАД", callback_data = "kafedra")],
          [InlineKeyboardButton("Можливості для студентів", callback_data = "mozhluv")],
          [InlineKeyboardButton("Умови вступу", callback_data = "umovy")]]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text('Hi!', reply_markup = reply)
    


def help(update, context):
    update.message.reply_text('Help!')

def kafedra(update, context):
    update.callback_query.message.reply_text('Прекрасная кафедра')
    
def umovy(update, context):
    update.callback_query.message.reply_text('Обери підпункт, який тобі цікавиий')
    
def teachers(update, context):
    update.callback_query.message.reply_text('...')

def education(update, context):
    update.callback_query.message.reply_text('...')

def history(update, context):
    update.callback_query.message.reply_text('...')

def classrooms(update, context):
    update.callback_query.message.reply_text('...')

def graduates(update, context):
    update.callback_query.message.reply_text('...')

def mozhluv(update, context):
    
    kb1 = [[InlineKeyboardButton('Проєктне навчання',callback_data = (''))],
          [InlineKeyboardButton('Дуальна освіта', callback_data = (''))],
          [InlineKeyboardButton('Працевлаштування',callback_data = (''))],
          [InlineKeyboardButton('Практика',callback_data = (''))]]
    reply = InlineKeyboardMarkup(kb1)
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?', reply_markup = reply)


    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("1622026876:AAGSPO1cWixVtEb0Zw8PKJxNa-KfQUh7818", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(umovy, pattern = 'umovy'))
    dp.add_handler(CallbackQueryHandler(mozhluv, pattern = 'mozhluv'))
    
    dp.add_handler(CallbackQueryHandler(teachers, pattern = 'teachers'))
    dp.add_handler(CallbackQueryHandler(education, pattern = 'education'))
    dp.add_handler(CallbackQueryHandler(history, pattern = 'history'))
    dp.add_handler(CallbackQueryHandler(classrooms, pattern = 'classrooms'))
    dp.add_handler(CallbackQueryHandler(graduates, pattern = 'graduates'))

    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
