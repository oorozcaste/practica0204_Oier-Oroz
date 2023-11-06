precios = {"pan":1.40,"huevos" : 2.30, "cebolla": 0.85, "aceite" : 4.35}
erantzuna = input("que quieres? :")
unitateak = int(input("cuantas unidades quieres: "))
if erantzuna in precios:
    print(f"eñ coste total es de {precios[erantzuna]*unitateak} euros")
else:
    print("el producto no esta en la lista")