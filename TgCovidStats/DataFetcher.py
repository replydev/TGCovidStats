from pathlib import Path
import logging

from TgCovidStats.Config import Config
from TgCovidStats.Utils import download_file

class DataFetcher:

    def __init__(self,config: Config):
        data_folder = Path("data/")
        self.config = config
        self.italy_data_path = data_folder.joinpath("italy_data.json")
        self.regions_data_path = data_folder.joinpath("regions_data.json")
        self.province_data_path = data_folder.joinpath("province_data.json")

        
    def all_files_downloaded(self):
        return self.italy_data_path.exists() and self.regions_data_path.exists() and self.regions_data_path.exists()

    def download(self):
        if not self.all_files_downloaded() or self.config["force_download"]:
            logging.info("Downloading italy data...")
            download_file(self.config["italy_link"],self.italy_data_path)
            logging.info("Downloading regions data...")
            download_file(self.config["regions_link"],self.regions_data_path)
            logging.info("Downloading province data...")
            download_file(self.config["province_link"],self.province_data_path)
            logging.info("Download done.")
        else:
            logging.info("Skipping download becouse data folder is already populated")

        

    




