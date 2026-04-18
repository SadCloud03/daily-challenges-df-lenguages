// DIA 10
// Palíndromo: Escribir
// un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)

#include <iostream>
#include <string>
#include <cctype> // Para tolower

using namespace std;

// Función para verificar si una palabra es palíndroma
bool esPalindromo(const string& palabra) {
    int izquierda = 0;
    int derecha = palabra.length() - 1;

    while (izquierda < derecha) {
        // Convertir ambos caracteres a minúsculas antes de comparar
        char charIzquierda = tolower(palabra[izquierda]);
        char charDerecha = tolower(palabra[derecha]);

        // Ignorar caracteres que no son letras
        if (!isalpha(charIzquierda)) {
            izquierda++;
            continue;
        }
        if (!isalpha(charDerecha)) {
            derecha--;
            continue;
        }

        // Comparar caracteres
        if (charIzquierda != charDerecha) {
            return false; // No es palíndromo
        }

        izquierda++;
        derecha--;
    }

    return true; // Es palíndromo
}

int main() {
    string palabra;
    cout << "Ingrese una palabra: ";
    cin >> palabra;

    if (esPalindromo(palabra)) {
        cout << palabra << " es palindromo." << endl;
    } else {
        cout << palabra << " no es palindromo." << endl;
    }

    return 0;
}
