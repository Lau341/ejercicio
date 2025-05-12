import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("users.csv")

# Filtrar los datos de España
df_espana = df[df['pais'] == 'Spain']

# Mostrar los datos de España
print(df_espana)

# Contar la cantidad de masculinos y femeninos
genero_counts = df_espana['genero'].value_counts()

# Mostrar el conteo por género
print(genero_counts)

# Graficar el conteo de géneros en un gráfico de barras
genero_counts.plot(kind='bar', color=['pink', 'lightblue'])
plt.title('Cantidad de Masculinos y Femeninos en España')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)  # Mantener las etiquetas horizontales
plt.show()
