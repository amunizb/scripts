memo = {1:1}
def a(n):    
    if n in memo:
        return memo[n]
    else:
        k = n // 2
        if n % 2 == 0:
            memo[n] = 2 * a(k)
            return memo[n]
        else:
            memo[n] = a(k) - 3 * a(k+1)
            return memo[n]
N = 5 ** 12
print(4 - (2**11) * a(N))


