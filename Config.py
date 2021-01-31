import logging
import json
from pathlib import Path

from Utils import write_to_file

class Config:
    def __init__(self,config_dict: dict):
        self.italy_link: str = config_dict["italy_link"]
        self.regions_link: str = config_dict["regions_link"]
        self.province_link: str = config_dict["province_link"]
        self.bot_token: str = config_dict["bot_token"]
        self.force_download: bool = config_dict["force_download"]
        
def load_config(filepath: Path):
    logging.info("Loading config...")
    try:
        with open(filepath) as f:
            return json.loads(f.read())
    except FileNotFoundError:
        logging.info("File \"%s\" does not exists" % (filepath))
        create_sample_config(filepath)
        return None
        
def create_sample_config(filepath: Path):
    logging.info("Creating sample config, edit the bot_token attribute otherwise the programm will not work")
    sample_config = {
        "bot_token": "BOT_TOKEN",
        "italy_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json",
        "regions_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json",
        "province_link": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json",
        "force_download": False,
    }
    j = json.dumps(sample_config)
    write_to_file(j,filepath)

