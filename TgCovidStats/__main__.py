from pathlib import Path
import logging
import datetime

from TgCovidStats.Config import Config
from TgCovidStats.Utils import create_folder_if_not_exists
from TgCovidStats.TGBot import TGBot
from TgCovidStats.BotCommands import start_command,callback_handler
from TgCovidStats.Memory import init_memory,get_config
from TgCovidStats.Database.User_Manager import UserManager


def create_folders():
    create_folder_if_not_exists("data/")
    create_folder_if_not_exists("charts/")
    create_folder_if_not_exists("logs/")

def init_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("{0}/{1}.log".format("logs", datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.INFO)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    rootLogger.addHandler(consoleHandler)

def init_bot():
    bot = TGBot(get_config())
    bot.add_command_handler("/start",start_command)
    bot.add_callback_handler(callback_handler)
    bot.start()

def main():
    create_folders()
    init_logger()
    if not init_memory():
        logging.error("Initialization failed")
        return
    init_bot()


if __name__ == "__main__":
    main()