import numpy as np
import matplotlib.pyplot as plt
from math import factorial


x = np.arange(1, 101)
p = np.ones(len(x))
max_idx = None

for i in range(len(x)):
    for j in range(x[i] - 1):
        p[i] *= (365 - j) / 365

    p[i] *= (x[i] - 1) / 365

    if i > 0 and max_idx == None and p[i] < p[i-1]:
        max_idx = i - 1

plt.plot(x, p, linestyle='--')
plt.scatter(x, p, c='r', s=6)
plt.scatter(max_idx+1, p[max_idx], c='g', s=30, label='Best position')
plt.annotate(f'Position = {max_idx+1}, p={round(p[max_idx], 4)}', xy=(max_idx+4, p[max_idx]))
plt.xlabel('Position')
plt.ylabel('p')
plt.legend()
plt.title('Probability of winning')
plt.show()