import pandas as pd
df = pd.read_csv("users.csv")
print(df[(df["pais"] == "Canada") & (df["edad"] >= 30) & (df["nombre"])])