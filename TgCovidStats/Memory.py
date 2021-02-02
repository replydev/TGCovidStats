from pathlib import Path
import logging

from TgCovidStats.DataLoader import DataLoader

class Memory:

    def init(self):
        logging.info("Loading Italy JSON...")
        self.loaded_italy = DataLoader(Path("data/italy_data.json")).load()
        logging.info("Loading Regions JSON...")
        self.loaded_regions = DataLoader(Path("data/regions_data.json")).load()
        logging.info("Loading Province JSON...")
        self.loaded_province = DataLoader(Path("data/province_data.json")).load()


