from pathlib import Path
import logging

from TgCovidStats.DataLoader import DataLoader
from TgCovidStats.DataFetcher import DataFetcher
from TgCovidStats.UserManager import UserManager
from TgCovidStats.Config import load_config,Config

def load_json():
    global italy
    global regions
    global province
    logging.info("Loading Italy JSON...")
    italy = DataLoader(Path("data/italy_data.json")).load()
    logging.info("Loading Regions JSON...")
    regions = DataLoader(Path("data/regions_data.json")).load()
    logging.info("Loading Province JSON...")
    province = DataLoader(Path("data/province_data.json")).load()

def init_memory():
    global user_manager
    global italy
    global regions
    global province
    global config
    logging.info("Loading config...")
    config_d = load_config("config.json")
    if config_d is None:
        return False
    config = Config(config_d)
    logging.info("Connection to database...")
    user_manager = UserManager(config.database_username,config.database_password,config.database_name)
    data_fetcher = DataFetcher(config)
    data_fetcher.download()
    load_json()
    return True
    

def get_user_manager():
    global user_manager
    return user_manager

def get_italy():
    global italy
    return italy

def get_regions():
    global regions
    return regions

def get_province():
    global province
    return province

def get_config():
    global config
    return config

def set_bot(_bot):
    global bot
    bot = _bot

def get_bot():
    global bot
    return bot
 

