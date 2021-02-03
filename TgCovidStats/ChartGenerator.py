import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import dateparser
import logging
from pathlib import Path

from TgCovidStats.Utils import sha1_hex,get_region_name_from_code,get_province_name_from_code

class ChartGenerator:

    def __init__(self,data: list,attribute: str,bot_username,region_name,province_name):
        self.data = data
        self.attribute = attribute
        self.bot_username = bot_username
        self.region_name = region_name
        self.province_name = province_name
        
    def get_dates(self):
        dates = []
        if self.province_name != 0:
            for element in self.data:
                if self.province_name == element["codice_provincia"]:
                    dates.append(dateparser.parse(element["data"]))
        elif self.region_name != 0:
            for element in self.data:
                if self.region_name == element["codice_regione"]:
                    dates.append(dateparser.parse(element["data"]))
        else:
            for element in self.data:
                dates.append(dateparser.parse(element["data"]))
        return dates

    def get_values(self):
        values = []
        if self.province_name != 0:
            for element in self.data:
                if self.province_name == element["codice_provincia"]:
                    values.append(element[self.attribute])
        elif self.region_name != 0:
            for element in self.data:
                if self.region_name == element["codice_regione"]:
                    values.append(element[self.attribute])
        else:
            for element in self.data:
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

        if self.region_name == 0:
            return title + " - Italia - @" + self.bot_username
        elif self.province_name == 0:
            return title + " - " + get_region_name_from_code(self.region_name,self.data) + " - @" + self.bot_username  
        else:
            return title + " - " + get_province_name_from_code(self.province_name,self.data) + " - @" + self.bot_username

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

        