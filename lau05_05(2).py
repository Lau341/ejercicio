import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer archivo CSV
df = pd.read_csv("users.csv")

# Filtrar usuarios cuyo país sea Canadá
filtro = df[df["pais"] == "Canada"]

# Contar cuántos usuarios hay por cada edad y ordenar por edad
conteo_edades = filtro["edad"].value_counts().sort_index()

# Crear un mapa de colores (colormap)
colores = plt.cm.viridis(np.linspace(0, 1, len(conteo_edades)))

# Crear gráfico de barras con colores distintos por edad
plt.figure(figsize=(10, 6))
plt.bar(conteo_edades.index, conteo_edades.values, color=colores)
plt.xlabel("Edad")
plt.ylabel("Número de usuarios")
plt.title("Usuarios de Canadá por edad (colores por edad)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()