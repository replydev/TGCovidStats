from pathlib import Path
from threading import Thread
from time import sleep
import logging
import datetime
import schedule

from TgCovidStats.Config import Config
from TgCovidStats.Utils import create_folder_if_not_exists
from TgCovidStats.TGBot import TGBot
from TgCovidStats.BotCommands import start_command,callback_handler
from TgCovidStats.Memory import init_memory,get_config
from TgCovidStats.Database.User_Manager import UserManager
from TgCovidStats.Updater import update_data

def init_daily_update_thread(config: Config):
    schedule.every().day.at(config.update_time).do(update_data)
    t = Thread(name="Updater",target=pending_daily_thread)
    t.start()

def pending_daily_thread():
    while True:
        schedule.run_pending()
        sleep(25)

def create_folders():
    create_folder_if_not_exists("data/")
    create_folder_if_not_exists("charts/")
    create_folder_if_not_exists("logs/")

def init_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("{0}/{1}.log".format("logs", datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.INFO)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    rootLogger.addHandler(consoleHandler)
    rootLogger.setLevel(logging.INFO)

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
    init_daily_update_thread(get_config())
    init_bot()

if __name__ == "__main__":
    main()