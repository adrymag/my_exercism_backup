def factors(value):
    if value == 1:
        return []

    prime_factors = []
    
    while value % 2 == 0:
        prime_factors.append(2)
        value = int(value / 2)
    
    d = 3
    
    while value >= d * d:
        while value % d == 0:
            prime_factors.append(d)
            value = int(value / d)
        d = d + 2

    if value > 1:
        prime_factors.append(value)
    
    return prime_factors 