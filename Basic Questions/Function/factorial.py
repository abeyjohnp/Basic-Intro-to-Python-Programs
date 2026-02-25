def factorial(p):
    if p==1:
        return 1
    else:
        return(p*factorial(p-1))

print(factorial(6))
