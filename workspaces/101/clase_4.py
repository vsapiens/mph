miArreglo = [1,2,3,4,5,6,7,8,9,10]

print(miArreglo, len(miArreglo))
miArreglo.pop(1)
print(miArreglo, len(miArreglo))
miArreglo.pop(2)
print(miArreglo, len(miArreglo))
miArreglo.pop(3)
print(miArreglo, len(miArreglo))
miArreglo.pop(4)
print(miArreglo, len(miArreglo))
miArreglo.pop()
print(miArreglo, len(miArreglo))

fib = [1,1]

tmp = fib[-1] + fib[-2]
fib.append(tmp)
tmp = fib[-1] + fib[-2]
fib.append(tmp)
tmp = fib[-1] + fib[-2]
fib.append(tmp)
tmp = fib[-1] + fib[-2]
fib.append(tmp)
tmp = fib[-1] + fib[-2]
fib.append(tmp)
tmp = fib[-1] + fib[-2]
fib.append(tmp)
print(fib)