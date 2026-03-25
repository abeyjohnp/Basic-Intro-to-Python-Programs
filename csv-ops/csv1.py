import pandas as pd
df = pd.read_csv("test.csv")
print(df)

print(df["Name"].sort_values())

print(df.loc[df["Mark"].idxmax(),"Name"])

print(df.loc[df["Gender"]=="M","Name"])

print(df["Department"].unique())