from pathlib import Path
import logging

from Config import Config
from Utils import download_file

class DataFetcher:

    def __init__(self,config: Config):
        self.config = config
        self.data_path = Path("data/")
        self.data_path.mkdir(exist_ok=True)
        self.italy_data_path = self.data_path.joinpath("italy_data.json")
        self.regions_data_path = self.data_path.joinpath("regions_data.json")
        self.province_data_path = self.data_path.joinpath("province_data.json")

        
    def all_files_downloaded(self):
        return self.italy_data_path.exists() and self.regions_data_path.exists() and self.regions_data_path.exists()

    def download(self):
        if not self.all_files_downloaded() or self.config.force_download:
            logging.info("Downloading italy data...")
            download_file(self.config.italy_link,self.italy_data_path)
            logging.info("Downloading regions data...")
            download_file(self.config.regions_link,self.regions_data_path)
            logging.info("Downloading province data...")
            download_file(self.config.province_link,self.province_data_path)
            logging.info("Download done.")
        else:
            logging.info("Skipping download becouse data folder is already populated")

        

    




