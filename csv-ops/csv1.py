import pandas as pd
df = pd.read_csv("test.csv")
print("Total Dataset : ")
print(df)

n=7
print("First ",n,"records")
print(df.head(n)) #default is 5

#print(df["Name"].sort_values())

print("Name of topper : ")
print(df.loc[df["Mark"].idxmax(),"Name"]) #idx returns the index number of the topper, and based on that we need to get the Name

print("Females : ")
print(df.loc[df["Gender"]=="F","Name"]) #df.loc is used to retreive the value from the dataframe. 

print("Departments : ")
print(df["Department"].unique()) 

print("CGPA Values : ")
print(df["CGPA"].value_counts().sort_values())

print("Avg CGPA of each branch")
print(df.groupby("Department")["CGPA"].mean())

print(df.shape) #Finds the number of rows and columns