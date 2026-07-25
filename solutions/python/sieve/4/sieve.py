def primes(limit):
    if limit < 2:
        return []

    if limit == 2:
        return [2]

    p = list(range(2, limit + 1))  
    
    [p.remove(x) for x in p if x > 2 and x % 2 == 0]       

    [p.remove(x) for cp in range(3, limit+1, 2) if cp in p for x in p if x > cp and x % cp == 0 ]
                
    return p