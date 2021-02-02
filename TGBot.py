from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,CallbackQueryHandler, CallbackContext,Filters
import logging

from Utils import build_regex_from_list
 
class TGBot:

    def __init__(self,config):
        self.updater = Updater(config["bot_token"])

    def add_command_handler(self,command: str,function):
        if command.startswith('/'):
            command = command[1:]
        logging.debug("Adding command handler \"%s\"" % (command))
        self.updater.dispatcher.add_handler(CommandHandler(command,function))
    
    @DeprecationWarning
    def add_message_handler(self,function,messages_list):
        regex = build_regex_from_list(messages_list) # TODO Use messages list also in BotCommands.py
        self.updater.dispatcher.add_handler(MessageHandler(Filters.regex(regex),function))
    
    def add_callback_handler(self,function):
        self.updater.dispatcher.add_handler(CallbackQueryHandler(function))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()