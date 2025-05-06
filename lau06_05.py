import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("users.csv")

# Corregir el filtro
filtro = ((df["pais"].isin(["Canada", "Germany", "France"])) & 
          (df["edad"] >= 30) & 
          (df["nombre"].notnull()))

# Filtrar los datos
df_filtrado = df[filtro]

# Calcular edad promedio por país
edad_promedio = df_filtrado.groupby("pais")["edad"].mean()

# Colores personalizados para cada país
colores = ['skyblue', 'lightgreen', 'salmon']

# Graficar
edad_promedio.plot(kind="bar", color=colores)
plt.title("Edad promedio de usuarios mayores de 30 por país")
plt.xlabel("País")
plt.ylabel("Edad Promedio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()