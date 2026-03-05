A terminal based program maintains a constant control over the interactuins iwth the user.
A Gui program is event druven

> promts user to enter sucessivve inputs
> gui in any order

>input no change
>input can be changed

# STEPS IN CODING GUI PROGRAMS
1. Define a new class to represent the main appl window
2. Instrantiate classes of window like labels fields
3. Postion rhes components in thw window
4. Rgister a method for each component
5. Define these methods
6. Define a main function that gets invoked

# A template for all GUI Programs

class ApplicationName(EasyFrame):
    the init method feintion
    defintion of event handling methods

def main():
    ApplicatioName().mainloop() 
        #mainloop is a function used for gui based programs, it will remain open for such interactions

if __name__ == "__main__":
    main()