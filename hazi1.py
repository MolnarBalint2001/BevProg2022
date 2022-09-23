

texts = {
    "greet" : "Üdvözöljük a menüben, válasszon egy opciót!",
    "options" : "Nyomjon 0-át a betűszámlásós programhoz!\nNyomjon 1-et a mértékegységváltós programhoz!\nNyomjon 2-t a kilépeshez!\n",

}

def charCount():

    inWord = input("Adjon meg egy mondatot: ")
    d = {c:inWord.count(c) for c in set(inWord)}




    print(d)
    print(inWord[::-1])
    print(inWord.split(" "))



def calculator():

    accept = {"cm" : 2.54, "inch" : 2.54}
    value = input("Adjon meg egy számot és egy mértékegységet (cm/inch): ")


    if value.split(" ")[-1] not in list(accept.keys()):
        print("Not correct unit!")
        return 
    
    if value.split(" ")[-1] == list(accept.keys())[0]:
        r  = float(value.split(" ")[0])/accept["cm"]
        print("{:.2f} inches".format(r))
    else:
        r = float(value.split(" ")[0])*accept["inch"]
        print("{:.2f} cm".format(r))

def main():


    functions = {
        0:charCount,
        1:calculator,
        2:exit
    }

    while True:
        print(texts["greet"])
        print(texts["options"])

        choosedOption = int(input("Adja meg a navigáló kódot: "))

        if choosedOption in functions:
            functions[choosedOption]()
        else:
            print("Helytelen kód!")
            
if __name__ == "__main__":
    main()
  