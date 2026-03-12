nombres = []
i = 0
while i < 4:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    i += 1 

print("La cantidad de nombres es:", len(nombres))

for nombre in nombres:
    print(nombre)