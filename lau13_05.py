import pandas as pd
df = pd.read_csv("users.csv")
print("Hombres mayores de 50:", df[(df["edad"] > 50) & (df["genero"] == "male")]["nombre"])
print("Mujeres mayores de 50:", df[(df["edad"] > 50) & (df["genero"] == "female")]["nombre"])