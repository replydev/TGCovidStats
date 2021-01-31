from urllib.request import urlopen
from pathlib import Path
import shutil
import logging

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

def build_regex_from_list(l: list):
    s = "^("
    for element in l:
        s += element
        s += "|"
    s[len(s) - 1] = ")" #replace last char
    s += "$"
    return s
    
    