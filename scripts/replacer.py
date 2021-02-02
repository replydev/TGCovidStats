# This script was used to convert java ReplyKeyboardBuilder structures in python ones

def main():
    file = open("replace.txt")
    s = file.read()
    s = s.replace("ReplyKeyboardBuilder.createReply()","[").replace(".build()","]\n]").replace(".addText(","InlineKeyboardButton(").replace(".row()","],\n[").replace(")",",callback_data=\"veneto\"),").replace(";","")
    print(s)


main()
