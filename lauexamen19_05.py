import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("users.csv")

# Filtrar usuarios mayores de 20 años de los paises
paises = ["Spain", "France", "Turkey"]
filtrar_edad = (df['edad'] > 20) & (df['pais'].isin(paises))
usuarios_filtrados = df[filtrar_edad]

# Obtener nombres
nombres = usuarios_filtrados['nombre'].tolist()
print("Nombres de usuarios mayores de 20 años de España, Francia y Turquía:")
print(nombres)

# Contar géneros
conteo_genero = usuarios_filtrados['genero'].value_counts()

# Mostrar conteo
print("\nCantidad por género:")
print(conteo_genero)

# Graficar
plt.figure(figsize=(6, 4))
conteo_genero.plot(kind='bar', color=['lightgreen', 'yellow'])
plt.title('Distribución por género de usuarios mayores de 20 años')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()