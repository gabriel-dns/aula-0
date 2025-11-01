import matplotlib.pyplot as plt
import numpy as np


print("Iniciar")


x = np.arange(1, 11)
y1 = np.random.randint(1, 100, size=10)
y2 = np.random.randint(1, 100, size=10)


plt.figure(figsize=(6, 4))
plt.bar(x, y1, color='skyblue')
plt.title("Gráfico de Barras Aleatório")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x, y2, marker='o', color='orange')
plt.title("Gráfico de Linha Aleatório")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()