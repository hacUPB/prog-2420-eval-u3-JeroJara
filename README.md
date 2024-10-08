[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Jerónimo Jaramillo Rivera
ID:  000540650
---

## Título del Proyecto: 

## Descripción: 
El presente programa busca permitir a un grupo de usuarios apostar una suma de dinero (en pesos colombianos) a un equipo deportivo presente en un determinado campeonato. Además, los usuarios tendrán acceso a varios diccionarios en donde podrán comparar índices de victoria de cada equipo en el torneo en cuestión, permitiéndoles apostar de forma
limpia y a consciencia.

## Alcance: 

El programa se basa en dos funcionalidades básicas: permitir a varios usuarios apostar por uno o varios equipos con diferentes cantidades de dinero y comparar entre sus opciones.

Cabe resaltar que el programa, al no tener acceso directo a los resultados de ningún campeonato, no podrá establecer un ganador en una apuesta, por lo que solo servirá para establecer el monto total que será pagado al ganador, y para definir comparaciones útiles para los apostadores.

## Estructuras de Datos a Utilizar:

Se usarán diccionarios que enlisten las características (ratios de victorias) de cada equipo en un torneo específico. Es decir, se usarán varios diccionarios para comparar equipos deportivos en diversas competencias.

## Pseudocódigo: 

```
Inicio
    Diccionario_Torneo_1 = {Diccionarios de equipos que participen en el torneo 1, con sus respectivos ratios de victoria}
    Diccionario_Torneo_2 = {Diccionarios de equipos que participen en el torneo 2, con sus respectivos ratios de victoria}
    Diccionario_Torneo_3 = {Diccionarios de equipos que participen en el torneo 3, con sus respectivos ratios de victoria}

    opcion = entero(introducir(imprimir("Hola, queridos apostadores. Por favor, escriban el número de la opción que desean ejecutar: 
    1. Ver equipos y sus ratios de victorias.
    2. Realizar una apuesta en grupo.)))
    
    definir funcion_menu(opcion):
        si funcion == 1:
         introducir(imprimir("Escriba el número correspondiente a un torneo: 1.Torneo_1 2.Torneo_2 3.Torneo_3"))
        
Fin 
```





