# DIA 7
# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable 
# (entre 8 y 16 caracteres)
# que incluya letras mayúsculas, minúsculas, números y símbolos.

#bibliotecas:
import random
import string

#conjunto para contraseña:
contraseña = set()
contador = 0    
simbolos = ("-","_")
letra_elegida = random.choice(string.ascii_letters)


#funcion generadora de contraseñas:
def generador_contraseñas(contador, contraseña):

    while contador  <= 17:
        letra_elegida = random.choice(string.ascii_letters)
        contraseña.add(letra_elegida)
        contador = contador + 1
        contraseña.add(str(random.randint(-1,9)))
        contador = contador + 1
        contraseña.add(random.choice(simbolos))
        contador = contador + 1

    contraseña = ''.join(contraseña)

    print(f"\n la contraseña es: {contraseña}")

#terminal 
while True:

    print(f"\nbienvenido al generador de contraseñas:","\n")
    print("Desea generar una contraseña: ")
    opcion_usu = str(input())
    opcion_usu = opcion_usu.lower()

    if "si" in opcion_usu:
        generador_contraseñas(contador, contraseña)
        break
    else:
        break
    