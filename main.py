from pathlib import Path

from DataFetcher import DataFetcher
from DataLoader import DataLoader
from ChartGenerator import ChartGenerator
from Config import Config,load_config
from Utils import create_folder_if_not_exists
from TGBot import TGBot
from BotCommands import start_command,callback_handler
from Memory import Memory


def create_folders():
    create_folder_if_not_exists("data/")
    create_folder_if_not_exists("charts/")


def init_bot(config: Config):
    bot = TGBot(config)
    bot.add_command_handler("/start",start_command)
    bot.add_callback_handler(callback_handler)
    bot.start()
    



def main():
    create_folders()
    config = load_config("config.json")
    if config is None:
        return
    data_fetcher = DataFetcher(config)
    data_fetcher.download()
    memory = Memory()
    init_bot(config)
    #chart_generator = ChartGenerator(loaded_italy,"terapia_intensiva",config["bot_username"])
    #chart_generator.gen_chart()




if __name__ == "__main__":
    main()