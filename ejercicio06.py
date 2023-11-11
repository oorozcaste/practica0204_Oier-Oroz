ikasleak={}
respuesta = input("que opcion vas a elegir (1) Añadir alumno/a, (2) Eliminar alumno/a, (3)"
                  " Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar.")
while True:
     if respuesta == "1":
         izena = input('nombre del alumno ')
         abizenak= input('apellidos del alumno: ')
         zembakia = input('teléfono del añumno: ')
         posta = input('correo electrónico del alumno: ')
         aprobado = input('¿ha aprobado el modulo?(si/no): ')
         dni = input('Introduce DNI del alumno: ')

         ikaslea = {"izena":izena,"abizenak":abizenak,"zembakia":zembakia,"posta":posta,"aprobado":aprobado}
         ikasleak[dni] = ikaslea
         respuesta = input("que opcion vas a elegir (1) Añadir alumno/a, (2) Eliminar alumno/a, (3)"
                  " Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar.")
     elif respuesta == "2":
         borrado = input("dime el dni del alumno que desees borrar del classroom: ")
         if borrado in ikasleak:
             del ikasleak[borrado]
     elif respuesta =="3":
         datos = input("dime el dni del alumno sobre el que queiras saber: ")
         if datos in ikasleak:
             print(ikasleak[datos])
     elif respuesta == "4":
         for a, b in ikasleak.items():
             print(a,b[0])
     elif respuesta == "5":
         for z in ikasleak.values():
             if z == "si":
                 print()
    
     elif respuesta == "terminar":
         print ("gracias por usar nuestro programa") 
         break