import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import dateparser
import logging
from pathlib import Path
import ujson

from TgCovidStats import Utils

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
                    if element[self.attribute] is None:
                        continue
                    dates.append(dateparser.parse(element["data"]))
        elif self.region_name != 0:
            for element in self.data:
                if self.region_name == element["codice_regione"]:
                    if element[self.attribute] is None:
                        continue
                    dates.append(dateparser.parse(element["data"]))
        else:
            for element in self.data:
                if element[self.attribute] is None:
                    continue
                dates.append(dateparser.parse(element["data"]))
        return dates

    def get_values(self):
        values = []
        if self.province_name != 0:
            for element in self.data:
                if self.province_name == element["codice_provincia"]:
                    if element[self.attribute] is None:
                        continue
                    values.append(element[self.attribute])
        elif self.region_name != 0:
            for element in self.data:
                if self.region_name == element["codice_regione"]:
                    if element[self.attribute] is None:
                        continue
                    values.append(element[self.attribute])
        else:
            for element in self.data:
                if element[self.attribute] is None:
                    continue
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
            return title + " - " + Utils.get_region_name_from_code(self.region_name,self.data) + " - @" + self.bot_username  
        else:
            return title + " - " + Utils.get_province_name_from_code(self.province_name,self.data) + " - @" + self.bot_username
    
    def read_values_from_cache(self,chart_folder_path: Path):
        json = Utils.read_file_content(chart_folder_path.joinpath("data.json"))
        d = ujson.loads(json)
        return d["last_value"],d["last_date"]


    def gen_chart(self):
        chart_title = self.get_title()
        chart_hash = Utils.sha1_hex(chart_title)
        chart_folder_path = Path("cache").joinpath(chart_hash)
        charts_image_path = chart_folder_path.joinpath("chart.png")
        if chart_folder_path.exists():
            last_value,last_date = self.read_values_from_cache(chart_folder_path)
            logging.debug("Chart already cached: %s" % (chart_title))
            return charts_image_path,last_value,last_date
        
        logging.debug("Generating chart: %s" % (self.attribute))
        Utils.create_folder_if_not_exists(chart_folder_path)
        dates = self.get_dates()
        values = self.get_values()

        if len(dates) != len(values):
            return None,None,None
        
        fig, ax = plt.subplots()
        ax.plot(dates, values)
        #ax.annotate("Ultimo valore: %.2f" % (last_value),xy=(10, 10), xycoords='figure pixels')
        #ax.annotate("Ultimo aggiornamento: %s" % (last_date.strftime("%d-%m-%Y")),xy=(370, 10), xycoords='figure pixels')
        ax.set(xlabel='Data', ylabel='Valore', title=chart_title)
        ax.grid()
        last_value = values[len(values) - 1]
        last_date = dates[len(dates) - 1].strftime("%d-%m-%Y")
        fig.savefig(charts_image_path)
        d = {
            "last_value": last_value,
            "last_date": last_date,
        }
        cache_json = ujson.dumps(d)
        Utils.write_to_file(cache_json,chart_folder_path.joinpath("data.json"))
        return charts_image_path,last_value,last_date
        #plt.show()

        