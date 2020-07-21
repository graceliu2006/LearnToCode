import time
print("Question 1")
# 1.

# Use loop and recursive function calls to implement factorial functions. 
# For recursive calls, print a line when each function is initialized and 
# another line before exit. Use time module to measure the running time of those 
# two functions.

# Examples: Factorial(5)=120

def factorial(number):
    product = 1
    for i in range (1,number+1):
        product *= i
    return product
start = time.time()   
print(factorial(10))
print(time.time() - start)

start = time.time()
print(factorial(200))
print(time.time() - start)  

start = time.time() 
print(factorial(100))
print(time.time() - start)

print("Question 2")
# 2.
# Use loop and recursive calls to calculate Fibonacci number. 
# For recursive calls, print a line when each function is initialized 
# and another line before exit. 
# Use time module to measure the running time of those two functions.
# Examples: Fibonacci(1)=1, Fibonacci(2)=1, Fibonacci(3)=2
# 1,1,2,3,5,8,13,21
def fibonacci(number):
    numbers = [0]
    fib = 0
    for i in range(1,number + 1):
        if i in range(1,3):
            fib = 1
            numbers.append(1)
        else:
            fib = (numbers[i-1]+numbers[i-2])
            numbers.append(numbers[i-1]+numbers[i-2])
    return (fib)

start = time.time()
print(fibonacci(100))
print(time.time() - start)

def fibonacci_simple(number):
    n1=1
    n2=1
    if number<3:
        return 1
    
    fib = 0
    for i in range(3,number + 1):
        fib = n1+n2
        n2=n1
        n1=fib
    
    return (fib)


start = time.time()   
print(fibonacci_simple(50))
print(time.time() - start)

start = time.time()
print(fibonacci_simple(100))
print(time.time() - start)  

start = time.time() 
print(fibonacci_simple(200))
print(time.time() - start)

start = time.time() 
print(fibonacci_simple(10))
print(time.time() - start)

def factorial_recursive(n):
    if n==0:
        return 1

    #print("Fact({}) is calling fact({})".format(n,n-1))
    result = n*factorial_recursive(n-1)
    #print(".....Fact({}) is here again".format(n))
    return result


start = time.time() 
print(factorial_recursive(10))
print(time.time() - start)



def fib_recursive(n):
    if n<3:
        return 1

    print("Fib({}) is calling fib({}) and fib({})".format(n,n-1,n-2))
    result = fib_recursive(n-1)+fib_recursive(n-2)
    print(".....Fib({}) is here again".format(n))
    return result

print(fib_recursive(100))