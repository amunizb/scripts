
dp = [[0] * 5 for _ in range(5)]
dp[-1][:-1] = [-100] * 4
for i in range(4):
    dp[i][-1] = 100

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        dp[i][j] = (dp[i+1][j] + dp[i][j+1]) / 2 

for row in range(4, -1, -1):
    print(dp[row])