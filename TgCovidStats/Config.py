import logging
import ujson
from pathlib import Path

from TgCovidStats.Utils import write_to_file

class Config:
    def __init__(self,config_dict: dict):
        self.italy_link: str = config_dict["italy_link"]
        self.regions_link: str = config_dict["regions_link"]
        self.province_link: str = config_dict["province_link"]
        self.bot_token: str = config_dict["bot_token"]
        self.bot_username: str = config_dict["bot_username"]
        self.force_download: bool = config_dict["force_download"]
        self.database_username: str = config_dict["database_username"]
        self.database_password: str = config_dict["database_password"]
        self.database_name: str = config_dict["database_name"]
        self.update_time: str = config_dict["update_time"]
        
def load_config(filepath: Path):
    try:
        with open(filepath) as f:
            return ujson.loads(f.read())
    except FileNotFoundError:
        logging.info("File \"%s\" does not exists" % (filepath))
        create_sample_config(filepath)
        return None
        
def create_sample_config(filepath: Path):
    logging.info("Creating sample config, edit the bot_token attribute otherwise the programm will not work")
    sample_config = {
        "database_username": "DATABASE_USERNAME",
        "database_password": "DATABASE_PASSWORD",
        "database_name": "DATABASE_NAME",
        "bot_token": "BOT_TOKEN",
        "bot_username": "BOT_USERNAME",
        "update_time": "18:30",
        "italy_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json",
        "regions_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json",
        "province_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json",
        "force_download": False,
    }
    j = ujson.dumps(sample_config,indent=4)
    write_to_file(j,filepath)

