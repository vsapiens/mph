# Clase 2 --- Visualización de Datos con Matplotlib

## Objetivo

Aprender a transformar datos en gráficos usando **Matplotlib**.

Los estudiantes aprenderán a crear: - Gráfico de barras - Gráfico de
línea - Gráfico de dispersión

Duración sugerida: - 40 min explicación - 20 min práctica

------------------------------------------------------------------------

## 1. Importar librerías

``` python
import pandas as pd
import matplotlib.pyplot as plt
```

------------------------------------------------------------------------

## 2. Dataset de ejemplo

``` python
datos = {
    "Nombre": ["Ana", "Luis", "Sofía", "Carlos", "Elena"],
    "Calificacion": [95, 88, 76, 90, 84],
    "Horas_estudio": [10, 7, 4, 8, 6]
}

df = pd.DataFrame(datos)
```

------------------------------------------------------------------------

## 3. Gráfico de barras

``` python
plt.bar(df["Nombre"], df["Calificacion"])
plt.title("Calificaciones por estudiante")
plt.xlabel("Nombre")
plt.ylabel("Calificación")
plt.show()
```

Sirve para **comparar valores entre categorías**.

------------------------------------------------------------------------

## 4. Gráfico de línea

``` python
plt.plot(df["Nombre"], df["Horas_estudio"], marker="o")
plt.title("Horas de estudio")
plt.xlabel("Estudiantes")
plt.ylabel("Horas")
plt.show()
```

Se usa para **ver tendencias**.

------------------------------------------------------------------------

## 5. Gráfico de dispersión

``` python
plt.scatter(df["Horas_estudio"], df["Calificacion"])
plt.title("Relación estudio vs calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.show()
```

Permite observar la relación entre dos variables.

------------------------------------------------------------------------

## Ejercicio

1.  Cambiar las horas de estudio.
2.  Cambiar algunas calificaciones.
3.  Crear nuevamente los tres gráficos.

Responder:

-   ¿Quién estudió más?
-   ¿Quién tiene la mejor calificación?
-   ¿Existe relación entre estudiar más y sacar mejor resultado?
