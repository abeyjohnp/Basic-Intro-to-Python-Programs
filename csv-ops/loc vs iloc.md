difference comes when name indexes comes

like 101,102,103 as index
df1.loc[1] - first row comes
df1.iloc[1] - first row coems

df1.loc[1,"Name"] 
but if iloc given same above error, iloc has a matrix type strucuture so give df1.iloc[1,0]