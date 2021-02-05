from TgCovidStats.InlineKeyboards import *
from TgCovidStats.Memory import get_user_manager,get_italy,get_regions,get_province,get_config
from TgCovidStats.ChartGenerator import ChartGenerator
from TgCovidStats.Utils import get_region_from_province

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,InputFile,InputMediaPhoto

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

def update_user_notifications(id: int,value: bool, query):
    user_manager = get_user_manager()
    user_manager.update_send_notifications(id,value)
    user = user_manager.get_user(id)
    query.edit_message_reply_markup(reply_markup=get_settings_keyboard(user.send_notifications))

def update_user(id: int,region: int,province: int, query):
    user_manager = get_user_manager()
    user_manager.update_region(id,region)
    user_manager.update_province(id,province)
    query.edit_message_reply_markup(reply_markup=get_start_keyboard())
    query.answer()

def start_command(update: Update, context: CallbackContext):
    user_manager = get_user_manager()
    id = update.effective_user.id
    user_manager.insert_user(id)
    # Reset user permission if he use /start command
    user_manager.update_region(id,0)
    user_manager.update_province(id,0)
    chart_generator = ChartGenerator(get_italy(),"totale_casi",get_config().bot_username,0,0)
    filename = chart_generator.gen_chart()
    update.message.reply_photo(photo=open(filename,'rb'), reply_markup=get_start_keyboard())

def callback_handler(update: Update, callback_context: CallbackContext):
    id = update.effective_user.id
    user_manager = get_user_manager()
    user = user_manager.get_user(id) #we are already sure that the user exists
    
    query = update.callback_query

    if query.data == "waiting":
        query.answer(text="⏱ Per favore attendi la generazione del grafico!",show_alert=True)
    elif query.data == "totale_positivi" or \
        query.data == "variazione_totale_positivi" or \
        query.data == "dimessi_guariti" or \
        query.data == "deceduti" or \
        query.data == "totale_positivi" or \
        query.data == "nuovi_positivi" or \
        query.data == "totale_casi" or \
        query.data == "tamponi" or \
        query.data == "tamponi_test_molecolare" or \
        query.data == "tamponi_test_antigenico_rapido" or \
        query.data == "ricoverati_con_sintomi" or \
        query.data == "terapia_intensiva" or \
        query.data == "totale_ospedalizzati" or \
        query.data == "isolamento_domiciliare":
            if user.selected_region == 0: # TODO User could be null if it send a callback without calling /start command
                l = get_italy()
            elif user.selected_province == 0:
                l = get_regions()
            else:
                if query.data != "totale_casi":
                    query.answer(text="‼️ Dati non disponibili per le provincie!",show_alert=True)
                    return
                l = get_province()
            query.edit_message_reply_markup(reply_markup=get_wait_keyboard())
            chart_generator = ChartGenerator(l,query.data,get_config().bot_username,user.selected_region,user.selected_province)
            filename,last_value,last_date = chart_generator.gen_chart()
            query.edit_message_media(media=InputMediaPhoto(media=open(filename,'rb')),caption="📉 Ultimo dato: %.2f\n📅 Data grafico: %s" % (last_value,last_date),reply_markup=get_start_keyboard())
            query.answer()

    
    elif query.data == "seleziona_regione":
        query.edit_message_reply_markup(reply_markup=get_regions_keyboard())
        query.answer()
    elif query.data == "seleziona_provincia":
        if user.selected_region == 0:
            query.answer(text="‼️ Seleziona prima una regione!",show_alert=True)
        else:
            #region_code = get_region_from_province(user.selected_province,get_province())
            region_code = user.selected_region
            if region_code == 13:
                query.edit_message_reply_markup(reply_markup=get_abruzzo_keyboard())
            elif region_code == 17:
                query.edit_message_reply_markup(reply_markup=get_basilicata_keyboard())
            elif region_code == 21:
                query.edit_message_reply_markup(reply_markup=get_bolzano_keyboard())
            elif region_code == 18:
                query.edit_message_reply_markup(reply_markup=get_calabria_keyboard())
            elif region_code == 15:
                query.edit_message_reply_markup(reply_markup=get_campania_keyboard())
            elif region_code == 8:
                query.edit_message_reply_markup(reply_markup=get_emilia_romagna_keyboard())
            elif region_code == 6:
                query.edit_message_reply_markup(reply_markup=get_friuli_venezia_giulia_keyboard())
            elif region_code == 12:
                query.edit_message_reply_markup(reply_markup=get_lazio_keyboard())
            elif region_code == 7:
                query.edit_message_reply_markup(reply_markup=get_liguria_leyboard())
            elif region_code == 3:
                query.edit_message_reply_markup(reply_markup=get_lombardia_keyboard())
            elif region_code == 11:
                query.edit_message_reply_markup(reply_markup=get_marche_keyboard())
            elif region_code == 14:
                query.edit_message_reply_markup(reply_markup=get_molise_keyboard())
            elif region_code == 1:
                query.edit_message_reply_markup(reply_markup=get_piemonte_keyboard())
            elif region_code == 16:
                query.edit_message_reply_markup(reply_markup=get_puglia_keyboard())
            elif region_code == 19:
                query.edit_message_reply_markup(reply_markup=get_sicilia_keyboard())
            elif region_code == 20:
                query.edit_message_reply_markup(reply_markup=get_sardegna_keyboard())
            elif region_code == 9:
                query.edit_message_reply_markup(reply_markup=get_toscana_keyboard())
            elif region_code == 22:
                query.edit_message_reply_markup(reply_markup=get_trento_keyboard())
            elif region_code == 10:
                query.edit_message_reply_markup(reply_markup=get_umbria_keyboard())
            elif region_code == 2:
                query.edit_message_reply_markup(reply_markup=get_valle_d_aosta_keyboard())
            elif region_code == 5:
                query.edit_message_reply_markup(reply_markup=get_veneto_keyboard())
            query.answer()

    elif query.data == "impostazioni":
        query.edit_message_reply_markup(reply_markup=get_settings_keyboard(user.send_notifications))
    elif query.data == "enable_notifications":
        update_user_notifications(id,True,query)
    elif query.data == "disable_notifications":
        update_user_notifications(id,False,query)
    elif query.data == "codice_sorgente":
        pass # TODO Implement
    elif query.data == "abruzzo":
        update_user(id,13,0,query)
    elif query.data == "basilicata":
        update_user(id,17,0,query)
    elif query.data == "bolzano":
        update_user(id,21,0,query)
    elif query.data == "calabria":
        update_user(id,18,0,query)
    elif query.data == "campania":
        update_user(id,15,0,query)
    elif query.data == "emilia-romagna":
        update_user(id,8,0,query)
    elif query.data == "friuli_venezia_giulia":
        update_user(id,6,0,query)
    elif query.data == "italia":
        update_user(id,0,0,query)
    elif query.data == "lazio":
        update_user(id,12,0,query)
    elif query.data == "liguria":
        update_user(id,7,0,query)
    elif query.data == "lombardia":
        update_user(id,3,0,query)
    elif query.data == "marche":
        update_user(id,11,0,query)
    elif query.data == "molise":
        update_user(id,14,0,query)
    elif query.data == "piemonte":
        update_user(id,1,0,query)
    elif query.data == "puglia":
        update_user(id,16,0,query)
    elif query.data == "sicilia":
        update_user(id,19,0,query)
    elif query.data == "sardegna":
        update_user(id,20,0,query)
    elif query.data == "toscana":
        update_user(id,9,0,query)
    elif query.data == "trento":
        update_user(id,22,0,query)
    elif query.data == "umbria":
        update_user(id,10,0,query)
    elif query.data == "valle_d_aosta":
        update_user(id,2,0,query)
    elif query.data == "veneto":
        update_user(id,5,0,query)
    elif query.data == "torna_indietro":
        query.edit_message_reply_markup(reply_markup=get_start_keyboard())
    elif query.data == "chieti":
        update_user(id,13,69,query)
    elif query.data == "l_aquila":
        update_user(id,13,66,query)
    elif query.data == "pescara":
        update_user(id,13,68,query)
    elif query.data == "teramo":
        update_user(id,13,67,query)
    elif query.data == "matera":
        update_user(id,17,77,query)
    elif query.data == "potenza":
        update_user(id,17,76,query)
    elif query.data == "bolzano":
        update_user(id,21,21,query)
    elif query.data == "catanzaro":
        update_user(id,18,79,query)
    elif query.data == "cosenza":
        update_user(id,18,78,query)
    elif query.data == "crotone":
        update_user(id,18,101,query)
    elif query.data == "reggio_di_calabria":
        update_user(id,18,80,query)
    elif query.data == "vibo_valentia":
        update_user(id,18,102,query)
    elif query.data == "avellino":
        update_user(id,15,64,query)
    elif query.data == "benevento":
        update_user(id,15,62,query)
    elif query.data == "caserta":
        update_user(id,15,61,query)
    elif query.data == "napoli":
        update_user(id,15,63,query)
    elif query.data == "salerno":
        update_user(id,15,65,query)
    elif query.data == "bologna":
        update_user(id,8,37,query)
    elif query.data == "ferrara":
        update_user(id,8,38,query)
    elif query.data == "forli-cesena":
        update_user(id,8,40,query)
    elif query.data == "modena":
        update_user(id,8,36,query)
    elif query.data == "parma":
        update_user(id,8,34,query)
    elif query.data == "piacenza":
        update_user(id,8,33,query)
    elif query.data == "ravenna":
        update_user(id,8,39,query)
    elif query.data == "reggio_dell_emilia":
        update_user(id,8,35,query)
    elif query.data == "gorizia":
        update_user(id,6,31,query)
    elif query.data == "pordenone":
        update_user(id,6,93,query)
    elif query.data == "trieste":
        update_user(id,6,32,query)
    elif query.data == "udine":
        update_user(id,12,30,query)
    elif query.data == "frosinone":
        update_user(id,12,60,query)
    elif query.data == "latina":
        update_user(id,12,59,query)
    elif query.data == "rieti":
        update_user(id,12,57,query)
    elif query.data == "roma":
        update_user(id,12,58,query)
    elif query.data == "viterbo":
        update_user(id,12,56,query)
    elif query.data == "genova":
        update_user(id,13,69,query)
    elif query.data == "imperia":
        update_user(id,7,10,query)
    elif query.data == "la_spezia":
        update_user(id,7,11,query)
    elif query.data == "savona":
        update_user(id,7,9,query)
    elif query.data == "bergamo":
        update_user(id,3,16,query)
    elif query.data == "brescia":
        update_user(id,3,17,query)
    elif query.data == "como":
        update_user(id,3,13,query)
    elif query.data == "cremona":
        update_user(id,3,19,query)
    elif query.data == "lecco":
        update_user(id,3,97,query)
    elif query.data == "lodi":
        update_user(id,3,98,query)
    elif query.data == "mantova":
        update_user(id,3,20,query)
    elif query.data == "milano":
        update_user(id,3,15,query)
    elif query.data == "monza_e_della_brianza":
        update_user(id,3,108,query)
    elif query.data == "pavia":
        update_user(id,3,18,query)
    elif query.data == "sondrio":
        update_user(id,3,14,query)
    elif query.data == "varese":
        update_user(id,3,12,query)
    elif query.data == "ancona":
        update_user(id,11,42,query)
    elif query.data == "ascoli_piceno":
        update_user(id,11,44,query)
    elif query.data == "fermo":
        update_user(id,11,109,query)
    elif query.data == "macerata":
        update_user(id,11,43,query)
    elif query.data == "pesaro_e_urbino":
        update_user(id,11,41,query)
    elif query.data == "campobasso":
        update_user(id,14,70,query)
    elif query.data == "isernia":
        update_user(id,14,94,query)
    elif query.data == "alessandria":
        update_user(id,1,6,query)
    elif query.data == "asti":
        update_user(id,1,5,query)
    elif query.data == "biella":
        update_user(id,1,96,query)
    elif query.data == "cuneo":
        update_user(id,1,4,query)
    elif query.data == "novara":
        update_user(id,1,3,query)
    elif query.data == "torino":
        update_user(id,1,1,query)
    elif query.data == "verbano_cusio_ossola":
        update_user(id,1,103,query)
    elif query.data == "vercelli":
        update_user(id,1,2,query)
    elif query.data == "bari":
        update_user(id,16,72,query)
    elif query.data == "barletta_andria_trani":
        update_user(id,16,110,query)
    elif query.data == "brindisi":
        update_user(id,16,74,query)
    elif query.data == "foggia":
        update_user(id,16,71,query)
    elif query.data == "lecce":
        update_user(id,16,75,query)
    elif query.data == "taranto":
        update_user(id,16,73,query)
    elif query.data == "cagliari":
        update_user(id,20,92,query)
    elif query.data == "nuoro":
        update_user(id,20,91,query)
    elif query.data == "sud_sardegna":
        update_user(id,20,111,query)
    elif query.data == "oristano":
        update_user(id,20,95,query)
    elif query.data == "sassari":
        update_user(id,20,90,query)
    elif query.data == "agrigento":
        update_user(id,19,84,query)
    elif query.data == "caltanissetta":
        update_user(id,19,85,query)
    elif query.data == "catania":
        update_user(id,19,87,query)
    elif query.data == "enna":
        update_user(id,19,86,query)
    elif query.data == "messina":
        update_user(id,19,83,query)
    elif query.data == "palermo":
        update_user(id,19,82,query)
    elif query.data == "ragusa":
        update_user(id,19,88,query)
    elif query.data == "siracusa":
        update_user(id,19,89,query)
    elif query.data == "trapani":
        update_user(id,19,81,query)
    elif query.data == "arezzo":
        update_user(id,9,51,query)
    elif query.data == "firenze":
        update_user(id,9,48,query)
    elif query.data == "grosseto":
        update_user(id,9,53,query)
    elif query.data == "livorno":
        update_user(id,9,49,query)
    elif query.data == "lucca":
        update_user(id,9,46,query)
    elif query.data == "massa_carrara":
        update_user(id,13,45,query)
    elif query.data == "pisa":
        update_user(id,9,50,query)
    elif query.data == "pistoia":
        update_user(id,9,47,query)
    elif query.data == "prato":
        update_user(id,9,100,query)
    elif query.data == "siena":
        update_user(id,13,52,query)
    elif query.data == "trento":
        update_user(id,22,22,query)
    elif query.data == "perugia":
        update_user(id,10,54,query)
    elif query.data == "terni":
        update_user(id,10,55,query)
    elif query.data == "aosta":
        update_user(id,2,7,query)
    elif query.data == "belluno":
        update_user(id,5,25,query)
    elif query.data == "padova":
        update_user(id,5,28,query)
    elif query.data == "rovigo":
        update_user(id,5,29,query)
    elif query.data == "treviso":
        update_user(id,5,26,query)
    elif query.data == "venezia":
        update_user(id,5,27,query)
    elif query.data == "verona":
        update_user(id,5,23,query)
    elif query.data == "vicenza":
        update_user(id,5,24,query)
    elif query.data == "nessuna_provincia":
        update_user(id,user.selected_region,0,query)
    
