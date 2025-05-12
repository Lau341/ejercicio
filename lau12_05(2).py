import pandas as pd
df = pd.read_csv("users.csv")
print(df[df["pais"] == "Australia"].sort_values(by="edad").head(5))