import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print(df ["math score"] + df ["reading score"] + df ["writing score"])