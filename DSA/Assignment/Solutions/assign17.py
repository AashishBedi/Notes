def sumn(n):
    if n == 0:
        return 0
    return n + sumn(n-1)

print(sumn(5))

def sumOddn(n):
    if n == 0:
        return 0
    return (2*n-1) + sumOddn(n-1)

print(sumOddn(5))


def sumEvenN(n):
    if n == 0:
        return 0
    return (2*n) + sumEvenN(n-1)

print(sumEvenN(5))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n
print(factorial(5))

def sum_squares(n):
    if n == 0:
        return 0
    return (n*n) + sum_squares(n-1)
print(sum_squares(5))