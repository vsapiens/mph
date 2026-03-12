# Clase 3 --- Análisis de Ventas de Bebidas

## Objetivo

Practicar Pandas y Matplotlib juntos usando un dataset de ventas semanales de bebidas.

Los estudiantes aprenderán a:
- Explorar datos con `head()` y `describe()`
- Crear un gráfico de línea
- Agrupar datos con `groupby`
- Crear un gráfico de barras con datos agrupados

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
    "dia": ["L", "M", "X", "J", "V", "S", "D"],
    "bebida": ["Café", "Café", "Té", "Café", "Té", "Smoothie", "Café"],
    "ventas": [18, 22, 14, 25, 16, 28, 20]
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

## 4. Gráfico de línea: ventas por día

``` python
plt.plot(df["dia"], df["ventas"], marker="o")
plt.title("Ventas por día")
plt.xlabel("Día")
plt.ylabel("Ventas")
plt.show()
```

Permite ver cómo cambian las ventas a lo largo de la semana.

------------------------------------------------------------------------

## 5. Agrupar datos con groupby

``` python
ventas_por_bebida = df.groupby("bebida")["ventas"].sum()
print(ventas_por_bebida)
```

`groupby` agrupa las filas por bebida y suma las ventas de cada una.

------------------------------------------------------------------------

## 6. Gráfico de barras: ventas totales por bebida

``` python
ventas_por_bebida.plot(kind="bar")
plt.title("Ventas totales por bebida")
plt.xlabel("Bebida")
plt.ylabel("Ventas")
plt.show()
```

------------------------------------------------------------------------

## Ejercicio

1. Cambiar algunas ventas o agregar un nuevo día.
2. Crear los dos gráficos nuevamente.
3. Escribir 1 conclusión (1–2 frases) sobre lo que observas en los datos.
