hiztegia = {}
while True:
    ingles = input("dime dos palabras en castellano en ingles,"
                   "las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas ")
    
    if ingles == "terminar":
        break

    bikoteak = ingles.split(",")

    for i in bikoteak:
        zatiak = i.split(":")
        gaztelania = zatiak[0]
        ingelesa = zatiak[1]
        hiztegia[gaztelania] = ingelesa
         
    

print(hiztegia)

esaldia = input("dime una frase en castellano: ")
esaldizatiak = esaldia.split()
hitzak_itzuliak = [hiztegia.get(hitza, hitza) for hitza in esaldizatiak]

itzulketa =" ".join(hitzak_itzuliak)

print("la frase traducida seria: ",itzulketa)