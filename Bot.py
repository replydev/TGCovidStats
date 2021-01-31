from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext,Filters
import logging

from Utils import build_regex_from_list
 
class Bot:

    def __init__(self,config):
        self.updater = Updater(config["bot_token"])

    def add_command_handler(self,command: str,function):
        logging.debug("Adding command handler \"%s\"" % (command))
        self.updater.dispatcher.add_handler(CommandHandler(command,function))
    
    def add_message_handler(self,function,messages_list):
        regex = build_regex_from_list(messages_list) # TODO Use messages list also in BotCommands.py
        self.updater.dispatcher.add_handler(MessageHandler(Filters.regex(regex),function))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()