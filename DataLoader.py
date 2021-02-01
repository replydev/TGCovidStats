from pathlib import Path
import json
import logging

class DataLoader:

    def __init__(self,filepath: Path):
        self.filepath = filepath

    def load(self):
        logging.debug("Tring to load %s" % (self.filepath))
        with open(self.filepath) as f:
            j = f.read()
            f.close()
            return json.loads(j)


