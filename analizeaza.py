import matplotlib.pyplot as plt
import numpy as np

# Anul 2022 --> +32 de locuri la buget (aprox +10%)
# Anul 2021 --> nota bac mate +10% (dificultate)

mediaAlex = 8.56

with open('note.txt', 'r') as f:
	data = f.read()

locuriBuget = 327
vector = data.split()

filtrat = []
for item in vector:
	if '.' in item:
		filtrat.append(item)

sortedData = sorted([float(item) for item in filtrat])
x=np.array(sortedData)
zece=sortedData.count(10)

plt.figure(figsize=(10,6))
plt.hist(x, bins=20, density=True, color='c', edgecolor='k', alpha=0.7)
plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1, label='Media generala')
plt.axvline(np.median(x), color='g', linestyle='dashed', linewidth=2, label='Median')
plt.axvline(mediaAlex, color='r', linestyle='solid', linewidth=1, label='Media lui Alex')
plt.xlabel("Nota admitere buget Calculatoare 2021 (327 de locuri)", fontsize=14)
plt.ylabel("Numar relativ de note", fontsize=12)
plt.title(f"Median:{np.median(x)} ||  Media generala:{x.mean():.2f} || Ultima nota:{x[0]} || {zece} de note cu 10")
plt.legend(loc="upper left")
plt.show()
print(zece)