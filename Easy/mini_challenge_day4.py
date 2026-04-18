# DIA 4
# Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

# hacer una lista vacia para los numeros.
numeros = set()

#hacer que el usuario pueda ingresar numero, ya sea enteros o fraccionarios. cuantos quiera:
while True:
    numero_usuario = input("ingrese un numero: ")
    if numero_usuario == "":
        break
    try:
        numero_conver_usuario = float(numero_usuario)
        numeros.add(numero_conver_usuario)
    except:
        print("ingrese numeros los cuales sean validos")

# convertir los valores de la lista "numeros a enteros":
numeros_entero = [int(numero) for numero in numeros]
print("la lista de numeros, en orden ascendente es: ", "\n", sorted(numeros_entero))

#