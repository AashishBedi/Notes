#Q1. Sorting an array
arr = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10]

arr.sort()
print("Sorted array is: ", arr)

#Q2. Removing non-int elements from the list
lst =  [10, "hello", 3.5, 7, True, 20, "Python"]
res = []

for i in lst:
    if type(i) == int:
        res.append(i)
print("New list of integers is: ", res)

#Q3. Calculate average of elements of a list
nums = [10, 20, 30, 40, 50]
total = 0
for n in nums:
    total += n
print("Average is: ", total/len(nums))

#Q4. Calculate the sum of digits of a number
num = 12345
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of digits is: ", sum)

#Q5. Create a list of first N prime numbers
n = int(input("Enter number: "))
primes = []
num = 2

while len(primes) < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print("First N prime numbers are: ", primes)

#Q6. Create a list of first N terms of Fibonacci series
n = int(input("Enter N: "))
fib = []
a, b = 0, 1

for i in range(n):
    fib.append(a)
    a, b = b, a+b
print("First N terms of Fibonacci series are: ", fib)

#Q7. Find the factorial of a number
num = int(input("Enter number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial is: ", fact)

