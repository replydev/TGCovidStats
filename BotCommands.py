from InlineKeyboards import get_start_keyboard

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Ciao, scegli un opzione: ", reply_markup=get_start_keyboard())

def callback_handler(update: Update, callback_context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "totale_positivi" or \
        query.data == "variazione_totale_positivi" or \
        query.data == "dimessi_guariti" or \
        query.data == "deceduti" or \
        query.data == "totale_casi" or \
        query.data == "nuovi_positivi" or \
        query.data == "tamponi" or \
        query.data == "tamponi_test_molecolare" or \
        query.data == "tamponi_test_antigenico_rapido" or \
        query.data == "ricoverati_con_sintomi" or \
        query.data == "terapia_intensiva" or \
        query.data == "totale_ospedalizzati" or \
        query.data == "isolamento_domiciliare":
            query.edit_message_text("Ahahahahah",reply_markup=get_start_keyboard())


    """
    elif query.data == "seleziona_regione":
    elif query.data == "seleziona_provincia":
    elif query.data == "impostazioni":
    elif query.data == "codice_sorgente":
    elif query.data == "abruzzo":
    elif query.data == "basilicata":
    elif query.data == "bolzano":
    elif query.data == "calabria":
    elif query.data == "campania":
    elif query.data == "emilia-romagna":
    elif query.data == "friuli_venezia_giulia":
    elif query.data == "italia":
    elif query.data == "lazio":
    elif query.data == "liguria":
    elif query.data == "lombardia":
    elif query.data == "marche":
    elif query.data == "molise":
    elif query.data == "piemonte":
    elif query.data == "puglia":
    elif query.data == "sicilia":
    elif query.data == "sardegna":
    elif query.data == "toscana":
    elif query.data == "trento":
    elif query.data == "umbria":
    elif query.data == "valle_d_aosta":
    elif query.data == "veneto":
    elif query.data == "torna_indietro":
    elif query.data == "":
    elif query.data == "chieti":
    elif query.data == "l_aquila":
    elif query.data == "pescara":
    elif query.data == "teramo":
    elif query.data == "matera":
    elif query.data == "potenza":
    elif query.data == "bolzano":
    elif query.data == "catanzaro":
    elif query.data == "cosenza":
    elif query.data == "crotone":
    elif query.data == "reggio_di_calabria":
    elif query.data == "vibo_valentia":
    elif query.data == "nessuna_provinicia":
    elif query.data == "avellino":
    elif query.data == "benevento":
    elif query.data == "caserta":
    elif query.data == "napoli":
    elif query.data == "salerno":
    elif query.data == "bologna":
    elif query.data == "ferrara":
    elif query.data == "forli-cesena":
    elif query.data == "modena":
    elif query.data == "parma":
    elif query.data == "piacenza":
    elif query.data == "ravenna":
    elif query.data == "reggio_dell_emilia":
    elif query.data == "veneto":
    elif query.data == "gorizia":
    elif query.data == "pordenone":
    elif query.data == "trieste":
    elif query.data == "udine":
    elif query.data == "nessuna_provinca":
    elif query.data == "frosinone":
    elif query.data == "latina":
    elif query.data == "rieti":
    elif query.data == "roma":
    elif query.data == "viterbo":
    elif query.data == "genova":
    elif query.data == "imperia":
    elif query.data == "la_spezia":
    elif query.data == "savona":
    elif query.data == "bergamo":
    elif query.data == "brescia":
    elif query.data == "como":
    elif query.data == "cremona":
    elif query.data == "lecco":
    elif query.data == "lodi":
    elif query.data == "mantova":
    elif query.data == "milano":
    elif query.data == "monza_e_della_brianza":
    elif query.data == "pavia":
    elif query.data == "sondrio":
    elif query.data == "varese":
    elif query.data == "ancona":
    elif query.data == "ascoli_piceno":
    elif query.data == "fermo":
    elif query.data == "macerata":
    elif query.data == "pesaro_e_urbino":
    elif query.data == "campobasso":
    elif query.data == "isernia":
    elif query.data == "alessandria":
    elif query.data == "asti":
    elif query.data == "biella":
    elif query.data == "cuneo":
    elif query.data == "novara":
    elif query.data == "torino":
    elif query.data == "verbano_cusio_ossola":
    elif query.data == "vercelli":
    elif query.data == "bari":
    elif query.data == "barletta_andria_trani":
    elif query.data == "brindisi":
    elif query.data == "foggia":
    elif query.data == "lecce":
    elif query.data == "taranto":
    elif query.data == "cagliari":
    elif query.data == "carbonia_iglesias":
    elif query.data == "medio_campidano":
    elif query.data == "nuoro":
    elif query.data == "ogliastra":
    elif query.data == "olbia_tempio":
    elif query.data == "oristano":
    elif query.data == "sassari":
    elif query.data == "agrigento":
    elif query.data == "caltanissetta":
    elif query.data == "catania":
    elif query.data == "enna":
    elif query.data == "messina":
    elif query.data == "palermo":
    elif query.data == "ragusa":
    elif query.data == "siracusa":
    elif query.data == "trapani":
    elif query.data == "arezzo":
    elif query.data == "firenze":
    elif query.data == "grosseto":
    elif query.data == "livorno":
    elif query.data == "lucca":
    elif query.data == "massa_carrara":
    elif query.data == "pisa":
    elif query.data == "pistoia":
    elif query.data == "prato":
    elif query.data == "siena":
    elif query.data == "trento":
    elif query.data == "perugia":
    elif query.data == "terni":
    elif query.data == "aosta":
    elif query.data == "belluno":
    elif query.data == "padova":
    elif query.data == "rovigo":
    elif query.data == "treviso":
    elif query.data == "venezia":
    elif query.data == "verona":
    elif query.data == "vicenza":
    elif query.data == "nessuna_provincia":
    """
