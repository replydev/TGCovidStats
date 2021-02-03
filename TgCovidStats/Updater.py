from TgCovidStats.Utils import delete_folder,create_folder_if_not_exists,sha1_hex,delete_file,move_file
from TgCovidStats.DataFetcher import DataFetcher
from TgCovidStats.Memory import get_config

import logging
from time import sleep

def open_and_hash(filename: str):
    f = open(filename)
    s = f.read()
    f.close()
    return sha1_hex(s)

def calculate_hash(italy_filename: str,regions_filename: str,province_filename: str):
    return open_and_hash(italy_filename),open_and_hash(regions_filename),open_and_hash(province_filename)

def update_data():
    logging.info("Preparing to update data..")
    logging.info("Deleting charts folder...")
    delete_folder("charts/")
    create_folder_if_not_exists("charts/")
    logging.info("Calculating data hash...")
    italy_hash,regions_hash,province_hash = calculate_hash("data/italy_data.json","data/regions_data.json","data/province_data.json")
    data_fetcher = DataFetcher(get_config())
    logging.info("Downloading new files...")
    data_fetcher.download(temp_file=True)
    logging.info("Calculating new data hash...")
    italy_temp_hash,regions_temp_hash,province_temp_hash = calculate_hash("data/italy_data_temp.json","data/regions_data_temp.json","data/province_data_temp.json")

    if italy_hash == italy_temp_hash and regions_hash == regions_temp_hash and province_hash == province_temp_hash:
        #Files are the same, delete the new files and wait 5 minutes
        logging.info("Same files, retrying in 5 minutes...")
        delete_file("data/italy_data_temp.json")
        delete_file("data/regions_data_temp.json")
        delete_file("data/province_data_temp.json")
        sleep(5 * 60 * 1000)
        update_data()
    else:
        logging.info("New file version detected! Overwriting...")
        move_file("data/italy_data_temp.json","data/italy_data.json")
        move_file("data/regions_data_temp.json","data/regions_data.json")
        move_file("data/province_data_temp.json","data/province_data.json")
        logging.info("Updating done!")

