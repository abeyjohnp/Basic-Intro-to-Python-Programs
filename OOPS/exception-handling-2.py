try:
    print(x)
except NameError:
    print("Not Present!")
else:
    print("Else!")
finally:
    print("All done!")