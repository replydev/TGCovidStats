from urllib.request import urlopen
from pathlib import Path
import shutil
import logging
import hashlib

def read_file_content(path: Path):
    try:
        with open(path) as f:
            logging.debug("Reading file: {}".format(path))
            content = f.read()
            f.close()
            return content
    except:
        logging.error("Failed to read file: {}".format(path))
        return None

def download_file(url: str, filename: Path):
    logging.debug("Downloading %s from %s" % (filename,url))
    with urlopen(url) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        out_file.close()

def write_to_file(text: str,filename: Path):
    logging.debug("Writing to file: %s" % (filename))
    with open(filename,'w') as f:
        f.write(text)
        f.close()

def sha1_hex(s: str):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()
    
def create_folder_if_not_exists(folder_path: str):
    p = Path(folder_path)
    p.mkdir(exist_ok=True)

def delete_folder(folder_path: str):
    shutil.rmtree(folder_path)

def delete_file(file_path: str):
    p = Path(file_path)
    p.unlink() # remove file

def move_file(from_path: str,to_path: str):
    from_file = Path(from_path)
    to_file = Path(to_path)
    from_file.replace(to_file) # replace overwrite the file

def get_region_from_province(province: int,data):
    for element in data:
        if element["codice_provincia"] == province:
            return element["codice_regione"]
    return None

def get_region_name_from_code(code: int, l):
    for element in l:
        if element["codice_regione"] == code:
            return element["denominazione_regione"]

def get_province_name_from_code(code: int, l):
    for element in l:
        if element["codice_provincia"] == code:
            return element["denominazione_provincia"]

    