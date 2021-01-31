from pathlib import Path

from DataFetcher import DataFetcher
from Config import Config,load_config


def create_folders()


def main():
    config = load_config("config.json")
    if config is None:
        return
    data_fetcher = DataFetcher(config)
    data_fetcher.download()



if __name__ == "__main__":
    main()