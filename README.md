[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Jerónimo Jaramillo Rivera
ID:  000540650
---

## Título del Proyecto: 

## Descripción: 
El presente programa busca permitir a un usuario apostar una suma de dinero (en pesos colombianos) a un conjunto deportivo presente en un determinado campeonato. Además, los usuarios tendrán acceso a una base de datos en donde podrán iniciar sesión, realizar, registrar y conocer la posible ganancia de sus apuestas con base en una cuota que ellos mismos podrán elegir, dentro de un rango predefinido.

## Alcance: 

El programa se basa en tres funcionalidades básicas: permitir a varios usuarios crear una cuenta en un sitio donde podrán registrar sus apuestas, además de ocnocer la posible suma de dinero a ganar.

Cabe resaltar que el programa, al no tener acceso directo a los resultados de ningún campeonato, no podrá establecer un ganador en una apuesta, por lo que solo servirá para establecer el monto total que será pagado al ganador, y para guardar sus apuestas previas en una cuenta donde podrán registrarse o iniciar sesión.

## Estructuras de Datos a Utilizar:

Se usarán diccionarios y listas que muestren los eventos, usuarios y apuestas realizadas.

## Pseudocódigo: 

```
Inicio

// Base de datos inicial
usuarios = {} //En el dicccioanrio de usuarios, la clave será el nombre del usuario y el valor será la contraseña
eventos = ["Copa Infantil de Futbol","Liga de Padel Amateur", "Ajedrez en el barrio", "Torneo de baloncesto callejero"] 
apuestas = []

FUNCION registrar_Usuario_nuevo(nombre, contraseña)
    si nombre no en usuarios:
        leer nuevo_Usuario 
        leer contraseña
        agregar nuevo_Usuario a usuarios
        imprimir("Usuario registrado exitosamente")
    si no:
         imprimir( "Nombre de usuario ya existe")
    fin si

funcion iniciar_Sesion(nombre, contraseña)
    mientras control == True:
        si nombre, contraseña en usuarios:
            print( "Inicio de sesión exitoso")
            control == False
        SINO:
            print("Nombre de usuario o contraseña incorrectos")   
        FIN SI
return control

FUNCIÓN realizar_Apuesta(usuario, evento_elegido, monto_apostar,cuota):
    posibleGanancia = monto_apostar * cuota
    añadir apuesta a la lista de apuestas del usuario
    imprimir("Apuesta realizada. Posible ganancia: " + posibleGanancia)

////////////////////////////////////////////////////////////////////////////////
imprimir("Bienvenido a JogaMuito, la mejor página de apuestas")

mientras True:
    imprimir( "1. Registrarse 2. Iniciar sesión 3. Salir")
    leer opcion
    si opcion == 1:
        leer nombre
        leer contraseña
        registrarUsuario(nombre, contraseña)
    si opcion == 2:
        nombre = leer nombre
        contraseña = leer contraseña
         iniciarSesion(nombre, contraseña):
           mientrassesiónActiva= True:
                imprimir( "1. Ver eventos disponibles 2. Realizar una apuesta" 3. Salir")
                leer seleccion
                si seleccion == 1:
                    print(eventos)
                si seleccion == 2:
                    print("Selecciona un evento:")
                    leer evento_elegido
                    print("Introduce la cantidad a apostar:")
                    leer monto_apostar
                    print("Escriba el monto al que quiere apostar. ¡Es un valor entre 1 y 2!")
                    leer cuota
                    si cuota en rango(1,3):
                        realizarApuesta(usuario, evento_elegido, monto_apostar,cuota)
                si seleccion == 3:
                    sesionActiva = false
                    print("Haz cerrado sesión. Esperamos que ganes todas tus apustas. ¡Suerte!")
                fin si
            fin mientras
    si opcion== 3:
        print("Has salido del sitio de apuestas. ¿No quieres ganar dinero fácil? Está bien.")
    fin si
Fin mientras

Fin

```





