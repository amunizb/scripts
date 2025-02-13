import numpy as np
import matplotlib.pyplot as plt

# Let X0 = 10 ** 100, Xn = R(X_{n-1}) where R(m) is a random number in 0,...,m-1
# We want to compute E[t] where t = min (n | Xn = 0)
# My computation says E[t] = S_X0 where S_n is the n-th cumulative sum of the pseudo-harmonic sequence (equal to harmonic sequence, but first term is 2)
# Let's check it
def pseudo_harmonic_sum(n):
    dp = [0] * (n+1)
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1/i 
    return dp
N = 10000

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 2
cum_sum = 2
for i in range(2, N + 1):
    dp[i] = (i + 1)/ i + cum_sum / i
    cum_sum += dp[i]

harmonic = pseudo_harmonic_sum(N)
plt.figure(figsize=(12,6))
plt.plot(range(N+1), dp, linestyle='--', marker='o', markersize=0.5, label='My result')
plt.scatter(range(N+1), harmonic, s=5, label='Quasi-harmonic sum', color='r')
plt.legend()
plt.title('Simulation')
plt.xlabel('Starting number')
plt.ylabel('Expected number of iterations to reach 0')
plt.show()

differences = np.abs(np.array(dp) - np.array(harmonic))
tol = 0.001
print('Your sequences agree' if (differences < tol).all() else "Your sequences don't agree")
