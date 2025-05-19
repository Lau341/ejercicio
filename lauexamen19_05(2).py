import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("users.csv")

# Filtrar usuarios entre 45 y 60 años
filtrar_edad = (df['edad'] >= 45) & (df['edad'] <= 60)
usuarios_filtrados = df[filtrar_edad]

# Contar por género
conteo_genero = usuarios_filtrados['genero'].value_counts()

# Mostrar resultados
print("Cantidad de usuarios entre 45 y 60 años por género:")
print(conteo_genero)

# Graficar
plt.figure(figsize=(6, 6))
conteo_genero.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['skyblue', 'lightpink'],
    labels=conteo_genero.index
)
plt.title('Distribución por género (usuarios de 45 a 60 años)')
plt.ylabel('')  # Quita el texto del eje Y
plt.tight_layout()
plt.show()
