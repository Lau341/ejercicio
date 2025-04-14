import pandas as pd
import numpy as np
a = np.random.randint(1,100 ,size=1000)
df = pd.read_csv("StudentsPerformance.csv")
df ["Columna de arreglo"] = a
print(df)