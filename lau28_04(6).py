import pandas as pd
df = pd.read_csv("users.csv")
print(df.groupby("genero")["nombre"].count())