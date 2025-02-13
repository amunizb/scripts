import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def uniform():
    rng = np.random.default_rng()
    t = rng.uniform()
    return t

def normal(x, mu=0, sigma=1):
    return 1/(np.sqrt(2*np.pi) * sigma) * np.exp(-(x-mu)**2 / (2*sigma**2))

def exponential(x):
    return np.exp(-x)

def inv_exp(t):
    return - np.log(1 - t)

def simulate_data(n, verbose=False):
    data = np.array([])
    while len(data) < n:
        t, x = uniform(), inv_exp(uniform())
        
        signal = normal(x) / (1.32 * exponential(x))
        if signal > t:
            positive = (np.random.uniform() < 1/2)
            if positive: 
                data = np.append(data, x)
            else:
                data = np.append(data, -x)

            if verbose and len(data) % 10 == 0:
                print(f'{len(data)} points found')
    
    return data

data = simulate_data(1000)

sns.histplot(data, kde=True, stat='density', label='Simulated distribution')
X = np.arange(min(data), max(data), 0.01)
Y = normal(X)
plt.plot(X, Y, label='Normal distribution', color='r')
plt.legend()
plt.show()
