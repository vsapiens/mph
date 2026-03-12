fib = [1,1]

n = int(input('Ingrese un número: '))
# range(10) = [0,1,2,3,4,5,6,7,8,9]
# range(2,10) = [2,3,4,5,6,7,8,9]
for i in range(2, n):
    tmp = fib[-1] + fib[-2]
    fib.append(tmp)


print(fib)