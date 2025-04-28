import pandas as pd
df = pd.read_csv("users.csv")
print(df[(df["edad"].between(40, 50))])