import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('nombres.csv')

# Mostrar las primeras filas del DataFrame
print(df['nombre'].head(100))