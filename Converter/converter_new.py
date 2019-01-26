import time

print("Pozdravljen, sem program, ki pretvarja kilometre v milje!")

while True:
    try:
        print("Vnesi število kilometrov, ki jih želiš pretvoriti: ")
        vnos = int(input())
    except ValueError:
        print("POZOR vnesti poizkušate črko. Vnesi številsko vrednost!")
        time.sleep(2) #vstavimo nek delay
        continue
    except:
        print("Nekaj se je zalomilo, napako bomo popravili v najkrajšem možnem času.")

    milje = vnos * 0.621371192

    print(f"Vaše število se pretvori v {milje:.2f} milje")

    nadaljevanje = input("Želiš nadaljevati: [y/n]")

    if nadaljevanje.lower() == "n":
        print("Hvala za vašo uporabo in lep pozdrav!")
        break



