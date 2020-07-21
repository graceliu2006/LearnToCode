def fact_func(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return(value)


def fact_recu(n):
    if n==0:
        return 1
    else:
        return fact_recu(n-1)*n

def fib_recu(n):
    if n==1 or n==2:
        return 1
    else:
        return fib_recu(n-1)+fib_recu(n-2)

def fib_func(n):
    value1=1
    value2=1
    if n<=2:
        return value1
    for i in range(2,n):
        new_value=value1+value2
        value1=value2
        value2=new_value
    return(value2)    


#print(fact_func(100))
#print(fact_recu(100))

print(fib_func(100))
print(fib_recu(100))

