def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end = ' ')

#printN(10)

def printNr(n):
    if n > 0:
        print(n, end = ' ')
        printNr(n-1)

#printNr(10)

def printoddN(n):
    if n > 0:
        printoddN(n-1)
        print(2*n-1, end = ' ')

#printoddN(10)
print('\n')
def printoddNr(n):
    if n > 0:
        print(2*n-1, end = ' ')
        printoddNr(n-1)

#printoddNr(10)

def printeven(n):
    if n > 0:
        printeven(n-1)
        print(2*n, end = ' ')

printeven(10)
print('\n')
def printevenr(n):
    if n > 0:
        print(2*n, end = ' ')
        printevenr(n-1)

printevenr(10)

