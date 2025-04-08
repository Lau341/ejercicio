#importar la libreria
import matplotlib.pyplot as plt

#datos
x = [1,2,3,4,5]
y = [10,20,30,40,50]

#graficar
plt.plot(x,y)

#etiquetas
plt.xlabel("Eje x: ")
plt.ylabel("Eje y: ")

#titulo
plt.title("Grafico de ejemplo: ")

#mostrar
plt.show()