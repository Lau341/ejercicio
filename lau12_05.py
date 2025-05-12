import pandas as pd
df = pd.read_csv("users.csv")
print(df[df["pais"] == "France"].sort_values(by="edad").head(5))