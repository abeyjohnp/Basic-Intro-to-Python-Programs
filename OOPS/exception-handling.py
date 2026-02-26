"""
    1. try:
        indented block
        #code
    2. except:
        indented block
        #code to handle exception
    3. else:
        indented block
    4. finally:
        indented block

ExceptionClasse:

    IOError (Exception)
    FileNotFoundError(Exception)
    IndexError (Lookup error)
    ZeroDivisionError (Arithmetic Error)
"""
#1
try:
    n=10
    d=0
    print(n/d)
except ZeroDivisionError: 
    print("Error, Division by 0")
#2
try:
    print(x)
except NameError: 
    print("No Name")
except:#this will work when we dont know which exception, so it works for all exception!
    print("Some exception occured!")

#3
try:
    print("Hello")
except:
    print("Some wrong!")
else: #if no exception
    print("Nothing went wrong")

#4
try:
    print("Hello")
except:
    print("Some wrong!")
else:
    print("Else!")
finally:
    print("Nothing went wrong - Finished Try Except")

#if at all no exception handled, it is handled by runtime! Finally will however print even if an error has occured,
#so if at all error occured, it will check finally, print that and then runtime error occurs.


