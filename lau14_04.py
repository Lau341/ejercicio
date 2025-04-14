import pandas as pd
import numpy as np
a = np.arange (0,1000)
df = pd.read_csv("StudentsPerformance.csv")
df ["Columna de arreglo"] = a
print(df)