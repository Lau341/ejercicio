import pandas as pd
df = pd.read_csv("users.csv")
print("Hombres:\n", df[df["pais"] == "United Kingdom"].sort_values(by="edad", ascending=False).head(20).query("genero == 'male'")[["nombre", "edad", "pais"]])
print("\nMujeres:\n", df[df["pais"] == "United Kingdom"].sort_values(by="edad", ascending=False).head(20).query("genero == 'female'")[["nombre", "edad", "pais"]])
