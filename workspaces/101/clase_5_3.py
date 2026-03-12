n = int(input('Ingrese un número: '))
fac = 1
# range(1, n+1) = [1,2,3,...,n]
for i in range(1, n+1):
    fac = fac * i # fac *= i
print(fac)