// DIA 9
// Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)

#include <iostream>
#include <algorithm>
#include <vector>

// por rasones de conpatibilidad por si acaso se asigna el espacio de nombre "std"
using namespace std;

// comienza el programa principal
int main() {
    // se crea el vector y declara que tipo de verctor es, en este caso es "int"
    // la variable vector se llama "vecto" y luego se le asigna los valores
    std::vector<int> vecto = {1, 2, 6, 9, 4, 3};

    // se usa "sort", funcion de "algorithm" para poder ordenar los numeros enteros dentro del vector
    std::sort(vecto.begin(), vecto.end());

    // espacio para que quede mas lindo
    std::cout << "\n" << "\n";

    // decir que se esta imprimiendo 
    std::cout << "los numeros ordenados son: ";
    
    // se itera "num" dentro de los elementos de vecto ya ordenado 
    for(int num : vecto) {
        // cada "num" se imprime con un espacio " " para que sea mas legible
        cout << num << " ";
    }
}