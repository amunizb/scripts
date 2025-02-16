import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(T, N, **kwargs):
    '''
    Simulates brownian motion over a
    time interval T with N steps
    '''
    dt = T / N
    rng = np.random.default_rng()

    W = np.zeros(N)
    
    for i in range(1, N):
        W[i] = W[i - 1] + rng.normal(scale = np.sqrt(dt))

    return W

def exp_brownian_motion(T, N, lamb):
    lamb = 0.2
    W = brownian_motion(T, N)
    log_Z = lamb * W - (1 / 2) * (lamb ** 2) * np.arange(N) * (T/N)
    Z = np.exp(log_Z)
    
    return Z


def montecarlo(process, ax, N_sim, **kwargs):
    W_final = []
    for _ in range(N_sim):
        W = process(kwargs.get('T', 10), kwargs.get('N', 100), lamb=kwargs.get('lamb', 0.5))
        ax.plot(W, linewidth=0.5)
        W_final.append(W[-1])
    return np.mean(W_final), np.std(W_final)


T = 10
N = 1000

fig, (ax0, ax1) = plt.subplots(1,2, figsize=(12,6))
fig.suptitle('Monte Carlo simulations')
ax0.set_title('Brownian motion')
ax1.set_title('Exponential brownian motion')

EW, STDW = montecarlo(brownian_motion, ax0, N_sim=10, T=T, N=N)
print(f'Time period T = {T}')
print(f'Mean of ending point of brownian motion = {EW:.4f} (expected = 0)')
print(f'Standard deviation of ending point of brownian motion = {STDW:.4f} (expected = {np.sqrt(T):.4f})')

EZ, STDZ = montecarlo(exp_brownian_motion, ax1, N_sim=10, T=T, N=N, lamb=2)
print(f'\nTime period T = {T}')
print(f'Mean of ending point of exponential brownian motion = {EZ:.4f} (expected = 1)')


plt.show()
