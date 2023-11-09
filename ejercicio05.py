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
esaldia = esaldia.split()
for u in esaldia:
    if u in hiztegia:
       u = hiztegia.keys(u)
print(esaldia)

   
