import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def play_game(p, N_max, b):
    f = p - (1 - p)/b

    N = 1
    wealth = [1]
    while N < N_max:
        toss = np.random.rand()
        if toss < p:
            wealth.append(wealth[-1]*(1 + f*b))
        else:
            wealth.append(wealth[-1]*(1 - f))
        N += 1
    return wealth

def monte_carlo(N_sim, p, N_max, b):
    final_wealth = []
    for i in range(N_sim):
        closing_price = play_game(p, N_max, b)[-1]
        final_wealth.append(closing_price)
    return final_wealth

def plot_wealth(N_sim):
    for i in range(N_sim):
        wealth = play_game(p, N_max, b)
        plt.plot(wealth, marker='o', ms=1, lw=0.5)
    plt.xlabel('Number of games')
    plt.ylabel('Wealth')
    plt.show()
     
def main_stats(simulation):
    simulation = np.array(simulation)
    mean = np.mean(simulation)
    std = np.std(simulation)
    min = np.min(simulation)
    max = np.max(simulation)
    return mean, std, min, max

#Input paramters
p = 0.6
b = 1
N_max = 10

#plot_wealth(N_sim=10)

simulation = monte_carlo(100, p, N_max, b)
mean, std, min, max = main_stats(simulation)

print(f"Mean: {mean:.2f}")
print(f"Standard deviation: {std:.2f}")
print(f"Minimum: {min:.2f}")
print(f"Maximum: {max:.2f}")


def plot_histogram(data):
    q1 = np.percentile(simulation, 25)
    q3 = np.percentile(simulation, 75)
    iqr = q3 - q1
    bin_width = 2 * iqr * len(simulation) ** (-1/3)
    N_bins = int((max - min) / bin_width)
    
    plt.figure(figsize=(12, 6))
    sns.histplot(simulation, bins='auto', kde=True, color='blue', alpha=0.6)
    plt.xlabel('Wealth at the end of simulation')
    plt.ylabel('Density')
    plt.title('Histogram of Wealth Distribution with KDE')
    plt.grid()
    plt.show()
    


zoom_simulation = [x for x in simulation if np.abs(x) < std]
plot_histogram(zoom_simulation)






