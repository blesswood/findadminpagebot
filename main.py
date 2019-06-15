# -*- coding: utf-8 -*-

import requests
import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

def result(sitename, bot, update):
	sitename = 'http://' + sitename
	file = open('main.txt')
	header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
	bot.send_message(chat_id=update.message.chat_id, text='Working, please wait')
	with file as f:
		for page in f:
			page = file.readline()
			siteresult = sitename + '/' + page
			response = requests.get(siteresult[:-1], headers=header)
			message = update.message
			if not response:
				dat = response.url + ' is wrong!'
				bot.send_message(chat_id=message.chat_id, text=dat)
			else:
				dat = str(response.url) + ' IS CORRECT, CONGRATZ!'
				bot.send_message(chat_id=message.chat_id, text=dat)
				break
	bot.send_message(chat_id=message.chat_id, text='Done')

	file.close()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token='800262026:AAE5TMuEPWbjpFJit_jb8mB4hPhZGysXjfk')
dispatcher = updater.dispatcher

def start(bot, update):
	message = update.message
	bot.send_message(chat_id=message.chat_id, text="Send me site address to find admin page")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def hang(bot, update):
	res = update.message.text
	result(res, bot, update)

msg_handler = MessageHandler(Filters.text, hang)
dispatcher.add_handler(msg_handler)

updater.start_polling()