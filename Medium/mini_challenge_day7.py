# DIA 6
# Juego de Piedra, Papel o Tijeras:
# Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

# voy a crear las funciones a utilizar 
# elegir aleatoriamente 
import random

# fincion de maquina, elegir movimiento 
def maquina(movimientos):
    movimiento_elegido = random.choice(movimientos)
    return movimiento_elegido 

# funcion del juego 
def ppt(eleccion_usuario, movimiento_maquina):
    if eleccion_usuario != movimiento_maquina:

        if movimiento_maquina == "tijera" and eleccion_usuario == "piedra":
            print("gano el usuario")
        elif movimiento_maquina == "piedra" and eleccion_usuario == "tijera":
            print("gano la maquina")

        elif movimiento_maquina == "papel" and eleccion_usuario == "piedra":
            print("gano la maquina")
        elif movimiento_maquina == "piedra" and eleccion_usuario == "papel":
            print("gano el usuario")
            
        elif movimiento_maquina == "papel" and eleccion_usuario == "tijera":
            print("gano el usuario")
        elif movimiento_maquina == "tijera" and eleccion_usuario == "papel":
            print("gano la maquina")
    else:
        print("ambas partes tuvieron la misma eleccion")



# crear la lista de movimientos
movimientos = ["piedra","papel","tijera"]

# hacer que el usuario ingrese su eleccion:
while True :
    print("elige Piedra, Papel o Tijera:","\n")
    eleccion_usuario = str(input("Que sacaras:"))
    eleccion_usuario = eleccion_usuario.lower()
    if eleccion_usuario in movimientos:
        break
    else:
        print("eleccion invalida, vuelve a intentar","\n")

# que la maquina elija su movimiento 
movimiento_maquina = maquina(movimientos)

#iniciar el juego "piedra, papel o tijeras"
ppt(eleccion_usuario, movimiento_maquina)

