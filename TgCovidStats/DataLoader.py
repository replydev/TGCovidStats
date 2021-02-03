from pathlib import Path
import ujson
import logging

class DataLoader:

    def __init__(self,filepath: Path):
        self.filepath = filepath

    def load(self):
        with open(self.filepath) as f:
            j = f.read()
            f.close()
            return ujson.loads(j)


