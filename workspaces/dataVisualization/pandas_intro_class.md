# Clase 1 --- Introducción a Pandas

## Objetivo

Aprender a usar **Pandas** para trabajar con datos en forma de tabla.

Al final de la clase los estudiantes podrán: - Crear un DataFrame -
Explorar datos - Filtrar información - Obtener estadísticas básicas

Duración sugerida: - 40 min explicación - 20 min práctica

------------------------------------------------------------------------

## 1. Importar Pandas

``` python
import pandas as pd
```

Explicar que `pd` es un alias común para la librería.

------------------------------------------------------------------------

## 2. Crear datos

``` python
datos = {
    "Nombre": ["Ana", "Luis", "Sofía", "Carlos", "Elena"],
    "Edad": [18, 17, 18, 19, 17],
    "Calificacion": [95, 88, 76, 90, 84],
    "Horas_estudio": [10, 7, 4, 8, 6]
}
```

Cada clave del diccionario representa una **columna**.

------------------------------------------------------------------------

## 3. Crear un DataFrame

``` python
df = pd.DataFrame(datos)
print(df)
```

Un **DataFrame** es una tabla similar a Excel.

------------------------------------------------------------------------

## 4. Explorar el DataFrame

Ver primeras filas:

``` python
df.head()
```

Ver columnas:

``` python
df.columns
```

Ver tamaño:

``` python
df.shape
```

------------------------------------------------------------------------

## 5. Seleccionar columnas

``` python
df["Nombre"]
```

Varias columnas:

``` python
df[["Nombre","Calificacion"]]
```

------------------------------------------------------------------------

## 6. Estadísticas básicas

Promedio:

``` python
df["Calificacion"].mean()
```

Máximo:

``` python
df["Calificacion"].max()
```

Mínimo:

``` python
df["Calificacion"].min()
```

------------------------------------------------------------------------

## 7. Filtrar datos

``` python
aprobados = df[df["Calificacion"] >= 85]
print(aprobados)
```

Esto devuelve solo los estudiantes con calificación mayor o igual a 85.

------------------------------------------------------------------------

## 8. Crear una nueva columna

``` python
df["Resultado"] = df["Calificacion"].apply(
    lambda x: "Aprobado" if x >= 70 else "Reprobado"
)
```

------------------------------------------------------------------------

## Ejercicio

1.  Agregar un nuevo estudiante.
2.  Cambiar algunas calificaciones.
3.  Encontrar:
    -   el promedio del grupo
    -   quién tiene la mejor calificación
