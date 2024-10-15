
def main():
    from os import system

# Base de datos inicial
usuarios = {}  # Diccionario de usuarios donde la clave es el nombre y el valor es la contraseña
eventos = ["1. Copa Infantil de Futbol", "2. Liga de Padel Amateur", "3. Ajedrez en el barrio", "4.Torneo de baloncesto callejero"]
apuestas = []

# Función para registrar un usuario nuevo
def registrar_usuario_nuevo(nombre, contraseña):
    if nombre not in usuarios:
        usuarios[nombre] = contraseña
        print("Usuario registrado exitosamente")
    else:
        print("Nombre de usuario ya existe. Por favor, inicie sesión con su contraseña")

# Función para iniciar sesión
def iniciar_sesion(nombre, contraseña):
    variable = True
    while variable == True:
        if nombre in usuarios and usuarios[nombre] == contraseña:
            print("Inicio de sesión exitoso. Seleccione una opción para continuar:")
            variable = False
        else:
            input("Nombre de usuario o contraseña incorrectos. Intente nuevamente:  ")
    return variable
        
# Función para realizar una apuesta
def realizar_apuesta(usuario, evento_elegido, monto_apostar, cuota):
    posible_ganancia = monto_apostar * cuota
# Se crea un diccionario en el que se almacena la informacion de las apuestas realizadas.
    apuestas.append({'usuario': usuario, 'evento': evento_elegido, 'monto': monto_apostar, 'cuota': cuota})
    print(f"Apuesta realizada. Posible ganancia: {posible_ganancia}")
    controlador = True
    while controlador == True: 
        if cuota in range(1.00,3.00):
            controlador == False
        else: 
            print("Por favor, ingrese una cuota válida entre 1 y 2")


# Inicio del programa
bandera = True
while bandera == True:
    print("¡Bienvenido a JogaMuito! la mejor página de apuestas")

    opcion = int(input("Selecciona una opción: \n 1. Iniciar sesión o registrarse \n 2. Salir \n "))

    if opcion == 1:

        nombre = input("Introduce tu nombre de usuario: ")

        contraseña = input("Introduce tu contraseña: ")
        
        variador = iniciar_sesion(nombre, contraseña)

        if variador == True:
            sesion_activa = True
            bandera = False

            while sesion_activa==True:

                seleccion = input(int("Selecciona una opción: \n 1. Ver eventos disponibles \n 2. Realizar una apuesta \n 3. Salir "))
                
                if seleccion == 1:
                    print("Eventos disponibles:", eventos)
                    sesion_activa = False
                    variador = False
                
                elif seleccion == 2:
                    evento_seleccionado = input(int("Selecciona un evento (escribe el número del evento):", eventos)) 
                    monto_apostar = input(float("Introduce la cantidad a apostar (COP): "))
                    cuota = input(float("Introduce la cuota (valor entre 1 y 1.5): "))
                    realizar_apuesta(nombre, evento_seleccionado, monto_apostar, cuota)
                    sesion_activa = False
                    variador = False
                
                elif seleccion == 3:
                    sesion_activa = False
                    print("Has cerrado sesión. ¡Suerte en tus apuestas!")
                    variador = False
                
            
        elif variador == False:
            print("Tu usuario no existe, así que debes registrarte: ")   
            nombre = input("Introduce tu nombre de usuario: ")
            contraseña = input("Introduce tu contraseña: ")
            registrar_usuario_nuevo(nombre, contraseña)
        bandera = False

    elif opcion == 2:
        print("Has salido del sitio de apuestas. ¡Vuelve pronto!")
        bandera = False

    

if __name__ == "__main__":
    main()
