#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
    int numestudiante = 0;
    cout << "¿Cuantos estudiantes tienes?" << endl;
    cin >> numestudiante;
    vector<string> nombres;     // Esto es equivalente a nombres = [] en python
    vector<int> calificaciones; // Esto es equivalente a calificaciones = [] en python
    int count = 1;
    // count 1, numestudiante = 20
    // 20 <= 1 => ni una sola vez => FALSE

    // count 1, numestudiante = 20
    // 1 <= 20 => si funciona => TRUE
    while (count <= numestudiante)
    {
        string nombre = "";
        // Nombre Estudiante
        cout << "Ingresa el nombre del estudiante #" << count << endl;
        cin >> nombre;
        nombres.push_back(nombre); // agregando a la lista
        // Calificacion del estudiante
        int calificacion = 0;
        cout << "¿Que calificacion saco " << nombre << "?" << endl;
        cin >> calificacion;
        calificaciones.push_back(calificacion); // agregando a la lista
        // Guardar información
        cout << "Guardado: " << nombre << "=>" << calificacion << endl;
        count++;
    }
    // Segunda parte
    char calificacionLetra;
    // nombre, calificacion
    for (int i = 0; i < nombres.size(); i++)
    {
        int calificacion = calificaciones[i];
        string nombre = nombres[i];
        cout << "El estudiante " << nombre << "saco una calificacion de ";
        if (calificacion >= 90)
        {
            cout << "A" << endl;
        }
        else if (80 <= calificacion && calificacion < 90)
        {
            cout << "B" << endl;
        }
        else if (70 <= calificacion && calificacion < 80)
        {
            cout << "C" << endl;
        }
        else if (60 <= calificacion && calificacion < 69)
        {
            cout << "D" << endl;
        }
        else
        {
            cout << "F" << endl;
        }
    }

    return 0;
};