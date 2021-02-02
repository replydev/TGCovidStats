import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import dateparser
import logging
from pathlib import Path

from TgCovidStats.Utils import sha1_hex

class ChartGenerator:

    def __init__(self,data: list,attribute: str,bot_username,region_name):
        self.data = data
        self.attribute = attribute
        self.bot_username = bot_username
        if region_name is None:
            self.region_name = "italia"
        else:
            self.region_name = region_name
        
    def get_dates(self):
        dates = []
        for element in self.data:
            if self.region_name != "italia":
                if self.region_name.lower() == element["denominazione_regione"].lower():
                    dates.append(dateparser.parse(element["data"]))
            else:
                dates.append(dateparser.parse(element["data"]))
            
        return dates

    def get_values(self):
        values = []
        for element in self.data:
            if self.region_name != "italia":
                if self.region_name.lower() == element["denominazione_regione"].lower():
                    values.append(element[self.attribute])
            else:
                values.append(element[self.attribute])
        return values

    def get_title(self):
        if self.attribute == "ricoverati_con_sintomi":
            title =  "Ricoverati con sintomi"
        elif self.attribute == "terapia_intensiva":
            title = "Terapia intensiva"
        elif self.attribute == "totale_ospedalizzati":
            title = "Totale ospedalizzati"
        elif self.attribute == "isolamento_domiciliare":
            title = "Isolamento domiciliare"
        elif self.attribute == "totale_positivi":
            title = "Totale positivi"
        elif self.attribute == "variazione_totale_positivi":
            title = "Variazione totale positivi"
        elif self.attribute == "nuovi_positivi":
            title = "Nuovi positivi"
        elif self.attribute == "dimessi_guariti":
            title = "Dimessi guariti"
        elif self.attribute == "deceduti":
            title = "Decessi"
        elif self.attribute == "totale_casi":
            title = "Totale casi"
        elif self.attribute == "nuovi_positivi":
            title = "Nuovi casi"
        elif self.attribute == "tamponi":
            title = "Tamponi"
        elif self.attribute == "tamponi_test_molecolare":
            title = "Tamponi test molecolare"
        elif self.attribute == "tamponi_test_antigenico_rapido":
            title = "Tamponi test antigenico"
        else:
            return None

        return title + " - " + self.region_name + " - " + self.bot_username

    def chart_exist(self,filename: str):
        p = Path("charts/")
        if not p.exists():
            return False
        return p.joinpath(filename).exists()

    def gen_chart(self):
        chart_title = self.get_title()
        chart_hash = sha1_hex(chart_title)
        charts_filename = chart_hash + ".png"
        if self.chart_exist(charts_filename):
            logging.debug("Chart already cached: %s" % (chart_title))
            return "charts/" + charts_filename
        
        logging.debug("Generating chart: %s" % (self.attribute))
        dates = self.get_dates()
        values = self.get_values()

        if len(dates) != len(values):
            return None
        
        fig, ax = plt.subplots()
        ax.plot(dates, values)
        ax.set(xlabel='Data', ylabel='Valore', title=chart_title)
        ax.grid()

        path = "charts/" + charts_filename
        fig.savefig(path)
        return path
        #plt.show()

        