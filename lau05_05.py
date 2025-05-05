import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("users.csv")
conteo_genero = df.groupby("genero")["nombre"].count()
plt.figure(figsize=(6, 6))
plt.pie(conteo_genero, labels=conteo_genero.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución por género')
plt.axis('equal')  # Hace que el círculo esté bien proporcionado
plt.show()