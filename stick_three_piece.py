import numpy as np
import matplotlib.pyplot as plt

def break_stick():
    x, y = np.random.rand(), np.random.rand()
    x, y = min(x, y), max(x, y)
    return x, y - x, 1 - y

def compute_mean(N):
    sum = 0
    mean = []
    for i in range(N):
        l1, l2, l3 = break_stick()
        sum += max(l1, l2, l3)
        mean.append(sum/(i+1))
    return mean

N = 10000
mean_series =  compute_mean(N)
plt.plot(range(1, N+1), mean_series, linewidth=1)
plt.axhline(11/18, color='r', linestyle='--')
plt.annotate('y = 11/18', (N-N/5, 11/18 + 0.01), color='r')
plt.show()
# print(f'Experimental mean = {mean_series[-1]}')
# print(f'11/18 = {11/18}')