divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
respuesta = input("dime el nombre de una divisa: ")
respuesta = respuesta.lower()
if respuesta in divisas :
    print(divisas[respuesta])
else:
    print("la divisa esta mal introducida")