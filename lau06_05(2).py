import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
df = pd.read_csv("StudentsPerformance.csv")

# Calcular el histograma manualmente
conteos, bins = np.histogram(df["math score"], bins=10)

# Calcular posiciones y anchos
bin_centers = 0.5 * (bins[1:] + bins[:-1])
anchos = np.diff(bins)

# Crear lista de colores (puede personalizarse más)
colores = plt.cm.viridis(np.linspace(0, 1, len(conteos)))

# Graficar usando plt.bar
plt.figure(figsize=(8, 5))
plt.bar(bin_centers, conteos, width=anchos, color=colores, edgecolor='black')
plt.title("Distribución de puntajes de Matemáticas")
plt.xlabel("Puntaje")
plt.ylabel("Cantidad de estudiantes")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
