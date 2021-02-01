from pathlib import Path

from DataFetcher import DataFetcher
from DataLoader import DataLoader
from ChartGenerator import ChartGenerator
from Config import Config,load_config
from Utils import create_folder_if_not_exists


def create_folders():
    create_folder_if_not_exists("data/")
    create_folder_if_not_exists("charts/")


def main():
    create_folders()
    config = load_config("config.json")
    if config is None:
        return
    data_fetcher = DataFetcher(config)
    data_fetcher.download()
    data_loader = DataLoader(Path("data/italy_data.json"))
    loaded_italy = data_loader.load()
    chart_generator = ChartGenerator(loaded_italy,"terapia_intensiva",config["bot_username"])
    chart_generator.gen_chart()



if __name__ == "__main__":
    main()