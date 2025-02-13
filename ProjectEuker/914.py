import numpy as np
import math

# def inradius(a, b):
#     return 0.5 * (a + b - (a**2 + b**2)**0.5)
def inradius(m, n):
    return n * (m - n)

def generate_pythagorean_triples(limit):
    triples = []
    parameters = []
    
    # Iterate over possible values of m and n
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            # m and n must satisfy the conditions for generating a primitive Pythagorean triple
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                # Calculate a, b, c
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                
                # Only add the triple if it's less than the limit and if inradius agrees 
                if c <= limit and abs(inradius(a, b)- 36) < 0.001:
                    triples.append((a, b, c))
                    parameters.append((m,n))
    return triples, parameters



def search(m, max_radius, outerradius):
    # Ensure triangle fits in circle
    bound = int((2*outerradius - m**2)**0.5)
    if m // 2 <  bound:
        n = m // 2

        if m % 2 == 0:
            n -= 1

        while math.gcd(n, m) != 1 and n > 1:
            n -= 2
        # a, b = m**2 - n**2, 2*m*n 
        r = inradius(m, n)
        if r > max_radius:
            print(f'Max radius updated with tuple (m,n) = {m,n}, inradius = {r}')
            max_radius = r

        n = m // 2
        if m % 2 == 0:
            n += 1
        while math.gcd(n, m) != 1 and n < m - 1 and n < bound:
            n += 2
        # a, b = m**2 - n**2, 2*m*n 
        r = inradius(m, n)
        if r > max_radius:
            print(f'Max radius updated with tuple (m,n) = {m,n}, inradius = {r}')
            max_radius = r
    else: 
        n = bound
        if (m - n) % 2 == 0:
            n -= 1
        while math.gcd(n, m) != 1 and n > 1:
            n -= 2
        # a, b = m**2 - n**2, 2*m*n 
        r = inradius(m, n)
        if r > max_radius:
            print(f'Max radius updated with tuple (m,n) = {m,n}, inradius = {r}')
            max_radius = r
    return max_radius 

outerradius = 10**12
max_radius = 0
start = int((2*outerradius)**0.5)
for m in range(start, -1, -1):
    max_radius = search(m, max_radius, outerradius)
print(max_radius)

    
        
    


# triples, parameters = generate_pythagorean_triples(200)
# print(triples, parameters)
# M, N = expand_triangle(parameters[0], 2*(10**18))
# A, B = M**2 - N**2, 2 * M * N
# max_inradius = inradius(A, B)
# print(max_inradius)
