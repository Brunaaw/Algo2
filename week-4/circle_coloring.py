MOD = 998244353

def power_mod(base, exp, mod):
    """ Calcula (base^exp) % mod usando exponenciação modular rápida. """
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_valid_colorings(N, M):
    """ Retorna o número de maneiras válidas de colorir o círculo. """
    if M == 1:
        return 0 
    
    total_ways = power_mod(M-1, N, MOD)
    
    if N % 2 == 0:
        total_ways = (total_ways + (M-1)) % MOD
    else:
        total_ways = (total_ways - (M-1)) % MOD
    
    return total_ways

N, M = map(int, input().split())

print(count_valid_colorings(N, M))
