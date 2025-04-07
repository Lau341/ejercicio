import pandas as pd     
df = pd.read_csv('StudentsPerformance.csv') 
print (df[['gender','math score']].head(40))
print (df[['gender','math score']].tail(15))
print (df[['gender','math score']].mean)
print (df[['gender','math score']].dtypes)
print(f'Número de filas y columnas: {df.shape}')