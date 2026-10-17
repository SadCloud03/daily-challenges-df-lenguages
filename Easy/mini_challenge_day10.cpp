// DIA 10
// Escribir un programa que simule un sistema para registrar  analizar las notas de un grupo de estudiantes 

/*Primero: preguntar por la cantidad de estudiantes
Segundo: iterar por la cantidad de estudiantes que se ingreso una funcion que pida el nombre y la nota del estudiante ingresado
Tercero: terminado la iteracion hacer una funcion que ordene las notas dependiendo de la nota que tengan
Cuarto: presentar las notas en la consola 

vector - estudiantes
vector - notas 
entero - cantidad_estudiantes

inicio:

    imprimir("ingresar la cantidad de estudiantes")
    almacenar el entero dentro de la variable "cantidad_estudiantes"
    
    por "cantidad_estudiantes":
        almacenar el nombre del estudiante en "estudiantes"
        almacenar la nota del estudiante en "notas"
        
    por cada "nota" dentro de "notas":
        revisar valor de esta y comparar entre las demas e ir descartando de notas a revisar segun estas se revisen
        revisar el nombre al cual pertenece la nota y tambien ordenar elv ector estudiantes

    por cada "nota" dentro de "notas":
        imprimir("{nombre} tiene {nota}") - esto de menor a mayor

fin
*/

// inicio de challenge:

// para manejar los strings 
#include <string>
// para manejar las entradas y salidas por terminal 
#include <iostream>
// para manejar listas sin tener que hacer nodos a mano 
#include <vector>
// para poder usar un algoritmo para ordenar de menor a mayor 
#include <algorithm>
// para poder encontrar las propiedades y limites fisicos de tipos de datos numericos 
#include <limits>

using namespace std;

// estructura para guardar al estudiante y su nota
struct Estudiante {
    string nombre;
    double nota;
};

int main() {
    int cantidad_estudiantes;

    cout << "Ingrese la cantidad de estudiantes de grado: ";
    if (!(cin >> cantidad_estudiantes) || cantidad_estudiantes <= 0) {
        cerr << "el valor puesto es invalido";
        return 1;
    };

    // Quitar del buffer el salto de linea que sobro de hacer cin int
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    //crear el vecto que contenga a todos los alumnos 
    vector<Estudiante> estudiantes;

    estudiantes.reserve(cantidad_estudiantes);

    for (int i = 0; i < cantidad_estudiantes; i++){
        Estudiante e;

        cout<< "ingrese el nombre del estudiante " << i + 1 << ": ";
        if (!getline(cin, e.nombre)) {
            cerr << "error al leer linea"; return 1;
        }

        cout << "ingrese la nota del estudiante: ";
        if (!(cin >> e.nota)) {
            cerr << "Error nota no valida";
            return 1;
        }

        //volvemos a borrar del buffer el salto de linea 
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        //metemos todo la estructura "e" dentro del vector "Estuantes"
        estudiantes.push_back(move(e));
    }

    stable_sort(estudiantes.begin(), estudiantes.end(), [](const Estudiante& a, const Estudiante& b) {
        return a.nota < b.nota; 
    });

    for (const auto& e : estudiantes) {
        cout << e.nombre << " tiene " << e.nota << "\n";
    }

    return 0;
}
 


