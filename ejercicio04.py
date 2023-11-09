hiztegia = {}
while True:
    dato = input("que dato nos vas a decir sobre ti: ")
    balorea = input("¿y cual seria el valor de ese dato?: ")
    hiztegia[dato] = balorea

    print(hiztegia)

    jarraipena = input("¿quieres continuar? (si/no)")  
    if jarraipena == "no":
        break