import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,8,11,14,17,20,23,26,29]

plt.scatter(x, y, color = "blue", marker="o" )
plt.title("Grafico: ")
plt.xlabel("Eje X: ")
plt.ylabel("Eje Y: ")
plt.show()