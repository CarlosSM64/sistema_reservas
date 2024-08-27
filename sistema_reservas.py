# Registrar usuario
# reservar un viaje
# ver reservas
# cancelar una reserva
#
usuarios = []
reservas = []

def menu_inicial():
    while True:
        print("Menú Principal")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar reservas")
        print("5. Salir")
        
        opcion = input("Seleccione un opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_viajes()
        elif opcion == "3":
            ver_reservas()
        elif opcion == "4":
            cancelar_reservas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo, por favor")
         
def registrar_usuario():
    
    nombre = input("Ingrese el usuario que quiere registrar: ")
    
    if nombre == usuarios:
        print("usuario ya registrado")
    else:
        usuario = {"usuario": nombre}
        usuarios.append(usuario)
        print(f"El usuario {nombre} ahora está registrado")
        print(usuario)
        return

def registrar_viajes():
    
    puntodepartida = input("Ingrese punto de partida: ")
    puntodellegada = input("Ingrese punto de llegada: ")
    fecha = str(input("Ingrese la fecha de la reserva: "))
    
    info = {"puntodepartida": puntodepartida, "puntodellegada": puntodellegada, "fecha": fecha}
    
    reservas.append(info)
    
    print(f"El punto de partida del viaje para el usuario es {puntodepartida} y su punto de llegada {puntodellegada} para el {fecha}")
    print(info)
    
def ver_reservas():
    for reservas1 in reservas:
        print(f"Nombre")
        
menu_inicial()