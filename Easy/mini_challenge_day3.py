# DIA 3
# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

# pedir al usuario que ingrese una palabra
palabra_usuario = str(input("escruibe una palabra: "))

#hacer una lista de vocales
vocales = ('a','e','i','o','u')

#lista vacia de las vocales dichas:
vocales_pal = set()

# hacer una funcion que se encargye de contar el numero de vocales en una cadena 
def contador_voc(palabra_usuario, vocales, vocales_pal):
    for letra in palabra_usuario:
        if letra in (vocales):
            vocales_pal.add(letra)
    return len(vocales_pal)

#probar
palabras = contador_voc(palabra_usuario, vocales, vocales_pal)

print(f"el numero de vocales es: {palabras}")