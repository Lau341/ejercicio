import pandas as pd
df = pd.read_csv("users.csv")
print(df[(df["pais"] == "Canada") | (df["pais"] == "Germany") | (df["pais"] == "France") & (df["edad"] >= 30) & (df["nombre"])])