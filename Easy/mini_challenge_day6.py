# DIA 5
# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

# decir el programa a hacer:
print("conversor de temperatura","\n")

# pedir al usuario que ingrese una temperatura en grados celsius:
temperatura_usuario = float(input("ingrese la temperatura, en grados celsius: "))

#hacer una funcion que convierta la temperatura que ingreso el usuario a fahrenheit
def conversor(temperatura_usuario):
    tem_convertida = (temperatura_usuario * 1.8) + 32
    return tem_convertida

#asignar la funcion a una variable 
temperatura_fahrenheit = conversor(temperatura_usuario)
 
#imprimir temperatura
print(f"la temperatura es, {temperatura_fahrenheit} grados fahrenheit")