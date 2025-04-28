import pandas as pd
df = pd.read_csv("users.csv")
print(df[df["pais"] == "Germany"].sort_values("edad", ascending=False).head(5))