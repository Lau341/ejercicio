import pandas as pd
df = pd.read_csv("users.csv")
print(df[df["genero"] == "female"].groupby("pais")["nombre"].count().sort_values(ascending=False).head(1))