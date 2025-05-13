import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("users.csv")

# Filtrar top 20 usuarios más viejos del Reino Unido
top_20_uk = df[df["pais"] == "United Kingdom"].sort_values(by="edad", ascending=False).head(20)

# Separar por género
hombres = top_20_uk[top_20_uk["genero"] == "male"]
mujeres = top_20_uk[top_20_uk["genero"] == "female"]

# Crear gráfico de barras horizontal
plt.figure(figsize=(10, 6))

# Graficar hombres
plt.barh(hombres["nombre"], hombres["edad"], color='blue', label='Hombres')

# Graficar mujeres
plt.barh(mujeres["nombre"], mujeres["edad"], color='pink', label='Mujeres')

# Ajustes visuales
plt.xlabel("Edad")
plt.ylabel("Nombre")
plt.title("Top 20 usuarios más viejos del Reino Unido por género")
plt.legend()
plt.gca().invert_yaxis()  # Para que el más viejo esté arriba
plt.tight_layout()
plt.show()
