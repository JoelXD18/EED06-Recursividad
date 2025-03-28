def factorialI (n):
    factorial = 1
    for i in range(2, n+1):
        factorial*=i
    return factorial

def factorialR(n):
    if n < 0:
        raise TypeError("No se puede obtener el factorial de valores negativos")
    if n <= 1:
        return 1
    else:
        return n * factorialR(n-1)
    



print("factorial(4):", factorialI(4))

def sumLista21(l):
    sumTotal=0
    for i in l:
        