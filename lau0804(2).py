import matplotlib.pyplot as plt
label = ["A","B","C","D"]
datos = [25,35,20,20]
color = ["gold","lightcoral","lightskyblue","lightgreen"]
plt.pie(datos, labels = label, colors = color, autopct = "%1.1F%%", startangle = 140)
plt.axis("equal")
plt.show()