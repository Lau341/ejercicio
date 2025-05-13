import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("users.csv")

# Filtrar mayores de 50
mayores_50 = df[df["edad"] > 50]

# Contar cuántos son de cada género
conteo_genero = mayores_50["genero"].value_counts()

# Crear gráfico de torta
plt.figure(figsize=(6, 6))
plt.pie(conteo_genero, labels=conteo_genero.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribución por género de usuarios mayores de 50 años")
plt.axis('equal')  # Para que el círculo no se vea ovalado
plt.show()
