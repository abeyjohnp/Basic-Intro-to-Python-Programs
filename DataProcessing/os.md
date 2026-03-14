# METHODS PRESENT IN OS MODULE
os.name - returns name of the os module that it imports
os.getcwd()
os.chdir()
os.listdir()
os.mkdir()
os.remove()
os.rename()
os.path.exists() - to check whether the path exists or not

# SYS MODULE

sys.version
sys.argv - arguments passed when executing a file
sys.path - paths where the folders will be searched while importing
sys.exit() - to exit the program

# INPUT AND OUTPUT USING SYS

a=sys.stdin.readline() - used to read ur string using the console
sys.stdout.write(a)

stderr - for standard error
print("Ex1", file=sys.stderr)