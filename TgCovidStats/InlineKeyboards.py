from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_wait_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("⏱ Attendi la generazione del grafico...",callback_data="waiting")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def get_start_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "⚠ Attualmente contagiati", callback_data="totale_positivi"
            ),
            InlineKeyboardButton(
                "⚠ Variazione totale positivi", callback_data="variazione_totale_positivi"
            ),
        ],
        [
            InlineKeyboardButton("💠 Guariti", callback_data="dimessi_guariti"),
            InlineKeyboardButton("😇 Decessi", callback_data="deceduti"),  
        ],
        [
            InlineKeyboardButton("‼️ Casi", callback_data="totale_casi"),
            InlineKeyboardButton("‼️ Nuovi casi", callback_data="nuovi_positivi"),
        ],
        [
            InlineKeyboardButton("💉 Tamponi", callback_data="tamponi"),
            InlineKeyboardButton("💉 Tamponi test molecolare", callback_data="tamponi_test_molecolare"),
        ],
        [
            InlineKeyboardButton("💉 Tamponi test antigenico", callback_data="tamponi_test_antigenico_rapido"),
            InlineKeyboardButton(
                "🤒 Ricoverati con sintomi", callback_data="ricoverati_con_sintomi"
            ),
        ],
        [
            InlineKeyboardButton(
                "🦠 Terapia intensiva", callback_data="terapia_intensiva"
            ),
            InlineKeyboardButton(
                "🏥 Totale ospedalizzati", callback_data="totale_ospedalizzati"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏠 Isolamento domiciliare", callback_data="isolamento_domiciliare"
            ),
        ],
        [
            InlineKeyboardButton(
                "🗻 Seleziona regione", callback_data="seleziona_regione"
            ),
            InlineKeyboardButton(
                "🏢 Seleziona provincia", callback_data="seleziona_provincia"
            ),
        ],
        [
            InlineKeyboardButton("🔧 Impostazioni", callback_data="impostazioni"),
            InlineKeyboardButton("💻 Codice sorgente", callback_data="codice_sorgente"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_regions_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Abruzzo", callback_data="abruzzo"),
            InlineKeyboardButton("Basilicata", callback_data="basilicata"),
            InlineKeyboardButton("P.A. Bolzano", callback_data="bolzano"),
        ],
        [
            InlineKeyboardButton("Calabria", callback_data="calabria"),
            InlineKeyboardButton("Campania", callback_data="campania"),
            InlineKeyboardButton("Emilia-Romagna", callback_data="emilia-romagna"),
        ],
        [
            InlineKeyboardButton(
                "Friuli Venezia Giulia", callback_data="friuli_venezia_giulia"
            ),
            InlineKeyboardButton("Italia", callback_data="italia"),
            InlineKeyboardButton("Lazio", callback_data="lazio"),
        ],
        [
            InlineKeyboardButton("Liguria", callback_data="liguria"),
            InlineKeyboardButton("Lombardia", callback_data="lombardia"),
            InlineKeyboardButton("Marche", callback_data="marche"),
        ],
        [
            InlineKeyboardButton("Molise", callback_data="molise"),
            InlineKeyboardButton("Piemonte", callback_data="piemonte"),
            InlineKeyboardButton("Puglia", callback_data="puglia"),
        ],
        [
            InlineKeyboardButton("Sicilia", callback_data="sicilia"),
            InlineKeyboardButton("Sardegna", callback_data="sardegna"),
            InlineKeyboardButton("Toscana", callback_data="toscana"),
        ],
        [
            InlineKeyboardButton("P.A. Trento", callback_data="trento"),
            InlineKeyboardButton("Umbria", callback_data="umbria"),
            InlineKeyboardButton("Valle d'Aosta", callback_data="valle_d_aosta"),
        ],
        [
            InlineKeyboardButton("Veneto", callback_data="veneto"),
            InlineKeyboardButton("🔙 Torna indietro", callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_abruzzo_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Chieti", callback_data="chieti"),
            InlineKeyboardButton("L'Aquila", callback_data="l_aquila"),
        ],
        [
            InlineKeyboardButton("Pescara", callback_data="pescara"),
            InlineKeyboardButton("Teramo", callback_data="teramo"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_basilicata_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Matera", callback_data="matera"),
            InlineKeyboardButton("Potenza", callback_data="potenza"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_bolzano_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Bolzano", callback_data="bolzano"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_calabria_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Catanzaro", callback_data="catanzaro"),
            InlineKeyboardButton("Cosenza", callback_data="cosenza"),
            InlineKeyboardButton("Crotone", callback_data="crotone"),
        ],
        [
            InlineKeyboardButton(
                "Reggio di Calabria", callback_data="reggio_di_calabria"
            ),
            InlineKeyboardButton("Vibo Valentia", callback_data="vibo_valentia"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provinicia"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_campania_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Avellino", callback_data="avellino"),
            InlineKeyboardButton("Benevento", callback_data="benevento"),
            InlineKeyboardButton("Caserta", callback_data="caserta"),
        ],
        [
            InlineKeyboardButton("Napoli", callback_data="napoli"),
            InlineKeyboardButton("Salerno", callback_data="salerno"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_emilia_romagna_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Bologna", callback_data="bologna"),
            InlineKeyboardButton("Ferrara", callback_data="ferrara"),
            InlineKeyboardButton("Forlì-Cesena", callback_data="forli-cesena"),
        ],
        [
            InlineKeyboardButton("Modena", callback_data="modena"),
            InlineKeyboardButton("Parma", callback_data="parma"),
        ],
        [
            InlineKeyboardButton("Piacenza", callback_data="piacenza"),
            InlineKeyboardButton("Ravenna", callback_data="ravenna"),
        ],
        [
            InlineKeyboardButton(
                "Reggio nell'Emilia", callback_data="reggio_dell_emilia"
            ),
            InlineKeyboardButton("Rimini", callback_data="veneto"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_friuli_venezia_giulia_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Gorizia", callback_data="gorizia"),
            InlineKeyboardButton("Pordenone", callback_data="pordenone"),
        ],
        [
            InlineKeyboardButton("Trieste", callback_data="trieste"),
            InlineKeyboardButton("Udine", callback_data="udine"),
        ],
        [
            InlineKeyboardButton("Nessuna provincia", callback_data="nessuna_provinca"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_lazio_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Frosinone", callback_data="frosinone"),
            InlineKeyboardButton("Latina", callback_data="latina"),
            InlineKeyboardButton("Rieti", callback_data="rieti"),
        ],
        [
            InlineKeyboardButton("Roma", callback_data="roma"),
            InlineKeyboardButton("Viterbo", callback_data="viterbo"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_liguria_leyboard():
    keyboard = [
        [
            InlineKeyboardButton("Genova", callback_data="genova"),
            InlineKeyboardButton("Imperia", callback_data="imperia"),
        ],
        [
            InlineKeyboardButton("La Spezia", callback_data="la_spezia"),
            InlineKeyboardButton("Savona", callback_data="savona"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_lombardia_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Bergamo", callback_data="bergamo"),
            InlineKeyboardButton("Brescia", callback_data="brescia"),
        ],
        [
            InlineKeyboardButton("Como", callback_data="como"),
            InlineKeyboardButton("Cremona", callback_data="cremona"),
        ],
        [
            InlineKeyboardButton("Lecco", callback_data="lecco"),
            InlineKeyboardButton("Lodi", callback_data="lodi"),
        ],
        [
            InlineKeyboardButton("Mantova", callback_data="mantova"),
            InlineKeyboardButton("Milano", callback_data="milano"),
        ],
        [
            InlineKeyboardButton(
                "Monza e della Brianza", callback_data="monza_e_della_brianza"
            ),
            InlineKeyboardButton("Pavia", callback_data="pavia"),
        ],
        [
            InlineKeyboardButton("Sondrio", callback_data="sondrio"),
            InlineKeyboardButton("Varese", callback_data="varese"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_marche_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Ancona", callback_data="ancona"),
            InlineKeyboardButton("Ascoli Piceno", callback_data="ascoli_piceno"),
            InlineKeyboardButton("Fermo", callback_data="fermo"),
        ],
        [
            InlineKeyboardButton("Macerata", callback_data="macerata"),
            InlineKeyboardButton("Pesaro e Urbino", callback_data="pesaro_e_urbino"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_molise_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Campobasso", callback_data="campobasso"),
        ],
        [
            InlineKeyboardButton("Isernia", callback_data="isernia"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_piemonte_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Alessandria", callback_data="alessandria"),
            InlineKeyboardButton("Asti", callback_data="asti"),
        ],
        [
            InlineKeyboardButton("Biella", callback_data="biella"),
            InlineKeyboardButton("Cuneo", callback_data="cuneo"),
        ],
        [
            InlineKeyboardButton("Novara", callback_data="novara"),
            InlineKeyboardButton("Torino", callback_data="torino"),
        ],
        [
            InlineKeyboardButton(
                "Verbano-Cusio-Ossola", callback_data="verbano_cusio_ossola"
            ),
            InlineKeyboardButton("Vercelli", callback_data="vercelli"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_puglia_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Bari", callback_data="bari"),
            InlineKeyboardButton(
                "Barletta-Andria-Trani", callback_data="barletta_andria_trani"
            ),
        ],
        [
            InlineKeyboardButton("Brindisi", callback_data="brindisi"),
            InlineKeyboardButton("Foggia", callback_data="foggia"),
        ],
        [
            InlineKeyboardButton("Lecce", callback_data="lecce"),
            InlineKeyboardButton("Taranto", callback_data="taranto"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_sardegna_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Cagliari", callback_data="cagliari"),
            InlineKeyboardButton("Nuoro", callback_data="nuoro"),
        ],
        [
            InlineKeyboardButton("Olbia-Tempio", callback_data="olbia_tempio"),
            InlineKeyboardButton("Oristano", callback_data="oristano"),
        ],
        [
            InlineKeyboardButton("Sassari", callback_data="sassari"),
            InlineKeyboardButton("Sud Sardegna", callback_data="sud_sardegna"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_sicilia_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Agrigento", callback_data="agrigento"),
            InlineKeyboardButton("Caltanissetta", callback_data="caltanissetta"),
            InlineKeyboardButton("Catania", callback_data="catania"),
        ],
        [
            InlineKeyboardButton("Enna", callback_data="enna"),
            InlineKeyboardButton("Messina", callback_data="messina"),
        ],
        [
            InlineKeyboardButton("Palermo", callback_data="palermo"),
            InlineKeyboardButton("Ragusa", callback_data="ragusa"),
        ],
        [
            InlineKeyboardButton("Siracusa", callback_data="siracusa"),
            InlineKeyboardButton("Trapani", callback_data="trapani"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_toscana_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Arezzo", callback_data="arezzo"),
            InlineKeyboardButton("Firenze", callback_data="firenze"),
        ],
        [
            InlineKeyboardButton("Grosseto", callback_data="grosseto"),
            InlineKeyboardButton("Livorno", callback_data="livorno"),
        ],
        [
            InlineKeyboardButton("Lucca", callback_data="lucca"),
            InlineKeyboardButton("Massa-Carrara", callback_data="massa_carrara"),
        ],
        [
            InlineKeyboardButton("Pisa", callback_data="pisa"),
            InlineKeyboardButton("Pistoia", callback_data="pistoia"),
        ],
        [
            InlineKeyboardButton("Prato", callback_data="prato"),
            InlineKeyboardButton("Siena", callback_data="siena"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_trento_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Trento", callback_data="trento"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_umbria_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Perugia", callback_data="perugia"),
            InlineKeyboardButton("Terni", callback_data="terni"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_valle_d_aosta_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Aosta", callback_data="aosta"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_veneto_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Belluno", callback_data="belluno"),
            InlineKeyboardButton("Padova", callback_data="padova"),
            InlineKeyboardButton("Rovigo", callback_data="rovigo"),
        ],
        [
            InlineKeyboardButton("Treviso", callback_data="treviso"),
            InlineKeyboardButton("Venezia", callback_data="venezia"),
        ],
        [
            InlineKeyboardButton("Verona", callback_data="verona"),
            InlineKeyboardButton("Vicenza", callback_data="vicenza"),
        ],
        [
            InlineKeyboardButton(
                "Nessuna provincia", callback_data="nessuna_provincia"
            ), InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def get_settings_keyboard(notify: bool):
    keyboard = [
        [
            InlineKeyboardButton("🔔 Invia notifiche",callback_data="useless"),
        ],
        [
            InlineKeyboardButton(text = "✅ Si" if notify else "Si",callback_data="enable_notifications"),
            InlineKeyboardButton(text = "No" if notify else "✅ No",callback_data="disable_notifications"),
        ],
        [
            InlineKeyboardButton("🔙 Torna indietro",callback_data="torna_indietro"),
        ],
    ]
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    return reply_keyboard