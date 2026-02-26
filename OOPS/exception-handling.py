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

try:
    n=10
    d=0
    print(n/d)
except ZeroDivisionError:
    print("Error, Division by 0")