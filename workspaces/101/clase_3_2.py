estatura = int(input("Ingrese su estatura en centimetros: "))
peso = int(input("Ingrese su peso en kilogramos: "))

estatura = estatura / 100  # Convertir estatura a metros
imc = peso / (estatura * estatura)

print("Su IMC es: ", imc)

if imc < 18.5:
    print("Bajo inferior")
elif  imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso")
else: 
    print("Obesidad")