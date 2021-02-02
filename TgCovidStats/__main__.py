from pathlib import Path

from TgCovidStats.DataFetcher import DataFetcher
from TgCovidStats.DataLoader import DataLoader
from TgCovidStats.ChartGenerator import ChartGenerator
from TgCovidStats.Config import Config,load_config
from TgCovidStats.Utils import create_folder_if_not_exists
from TgCovidStats.TGBot import TGBot
from TgCovidStats.BotCommands import start_command,callback_handler
from TgCovidStats.Memory import Memory


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