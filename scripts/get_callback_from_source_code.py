

def main():

    file = open("source.txt",encoding='cp850')
    output = open("attributes.txt",'w')

    for line in file.readlines():
        if "callback_data=" in line:
            args = line.split("callback_data=")
            output.write(args[1].replace("\"","").replace("),","")) #no need to put \n

    file.close()
    output.close()


main()