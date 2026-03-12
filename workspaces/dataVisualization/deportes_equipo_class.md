# Clase 4 --- Análisis de Rendimiento Deportivo

## Objetivo

Analizar datos deportivos para encontrar relaciones entre variables y comparar equipos.

Los estudiantes aprenderán a:
- Crear un gráfico de dispersión para buscar relaciones
- Usar `groupby` con `mean()` para promedios por grupo
- Crear un gráfico de barras con datos agrupados
- Escribir conclusiones y recomendaciones basadas en datos

Duración sugerida: - 40 min explicación - 20 min práctica

------------------------------------------------------------------------

## 1. Importar librerías

``` python
import pandas as pd
import matplotlib.pyplot as plt
```

------------------------------------------------------------------------

## 2. Crear el dataset

``` python
datos = {
    "estudiante": ["Ana", "Luis", "Mia", "Omar", "Sara", "Noah"],
    "horas_entreno": [2, 3, 1, 4, 2, 3],
    "puntos": [10, 14, 9, 18, 12, 15],
    "equipo": ["Azul", "Rojo", "Azul", "Verde", "Rojo", "Verde"]
}

df = pd.DataFrame(datos)
```

------------------------------------------------------------------------

## 3. Explorar los datos

``` python
df.head()
```

``` python
df.describe()
```

------------------------------------------------------------------------

## 4. Gráfico de dispersión: horas de entreno vs puntos

``` python
plt.scatter(df["horas_entreno"], df["puntos"])
plt.title("Horas de entreno vs Puntos")
plt.xlabel("Horas de entreno")
plt.ylabel("Puntos")
plt.show()
```

¿Hay relación? Si los puntos suben cuando las horas suben, hay una relación positiva.

------------------------------------------------------------------------

## 5. Agrupar datos: promedio de puntos por equipo

``` python
puntos_por_equipo = df.groupby("equipo")["puntos"].mean()
print(puntos_por_equipo)
```

`groupby` agrupa por equipo y `mean()` calcula el promedio de puntos de cada uno.

------------------------------------------------------------------------

## 6. Gráfico de barras: promedio de puntos por equipo

``` python
puntos_por_equipo.plot(kind="bar")
plt.title("Promedio de puntos por equipo")
plt.xlabel("Equipo")
plt.ylabel("Puntos (promedio)")
plt.show()
```

------------------------------------------------------------------------

## Ejercicio

1. Cambiar horas de entreno o puntos de algunos estudiantes.
2. Crear los dos gráficos nuevamente.
3. Escribir 1 conclusión (2 frases) sobre lo que observas en los datos.
4. Escribir 1 recomendación basada en los resultados.
