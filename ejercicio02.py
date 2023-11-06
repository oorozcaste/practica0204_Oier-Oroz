izena = input("nombre: ")
adina = input("tu edad: ")
helbidea = input("tu direccion: ")
zembakia = input("tu numero de telfono: ")
datuak = { "nombre": izena,"edad" : adina,"dirección" : helbidea,
          "numero" : zembakia}

print(F"{datuak['nombre']} de {datuak['edad']} años de edad vive en {datuak['dirección']} y su numero es {datuak['numero']}")