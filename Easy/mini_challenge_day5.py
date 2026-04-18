#DIA 5
#Crear un Diccionario:
#Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

# crear dos listas para el diccionario:
local = ["casa", "edificio", "cabaña", "granja"]
numero = [1831, 4565, 3423, 4582]

#crear la funcion que verifique si se puede hacer el diccionario y haga el diccionario
def diccionario(local, numero):
    # confirmar si la lista local y numero tienen la misma cantidad de elementos
    if len(local) == len(numero):
        
        #crear el diccionario
        diccionario = {}

        #iterar sobre local para hacer que cada elemento de local tenga asociado un numero
        # for lugar in range(len(local)):
        for local, numero in zip(local, numero): #con zip se puede hacer mas rapido 

            # #hacer que cada lugar(elemento) en local sea una clave
            # clave = local[lugar]
            # #hacer que cada lugar en numero sea una llave
            # llave = numero[lugar]

            #agregar al diccionario creado con anterioridad la clave y la llave como valor de la clave 
            # diccionario[clave] = llave
            diccionario[local] = numero #al usar zip tuve que cambiar todo lo anterior
            #ni idea de que en python se podian asignar elementos asi de facil en una lista 
    
    return diccionario

diccionario_creado = diccionario(local,numero)
print(diccionario_creado)


local_fin = diccionario(local, numero)
print(local_fin)