# DIA 2
# Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

# pedir que el usuario ingrese un numero 
num_usuario = int(input("escribe un numero el cual quieras saber su tabla de multiplicar: "))

# funcion que requiera del numero:
def tabla_mul(num_usuario):
    for i in range(1, 11):
        num_multiplicado = num_usuario * i
        print(num_multiplicado)

tabla_de_multiplicar = tabla_mul(num_usuario)
print(f"La tabla del {num_usuario}, es:")
print(tabla_de_multiplicar)