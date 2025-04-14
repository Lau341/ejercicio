import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print (df ["math score"].sum())
print (df ["math score"].count())
print (df ["math score"].mean())
print (df ["math score"].std())
print (df ["math score"].max())
print (df ["math score"].min())