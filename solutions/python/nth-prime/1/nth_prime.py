import math

def primes(limit):
    if limit < 2:
        return []
    if limit == 2:
        return [2]
    if limit in [3, 4]:
        return [2,3]
    if limit in [5, 6]:
        return [2,3,5]
    if limit in [7, 8, 9, 10]:
        return [2,3,5,7]
    # if limit in [11,12]:
    #     return [2,3,5,7,11]

    sqrt0 = int(math.sqrt(limit))
    print(sqrt0)
    p0 = [2] + list(range(3, sqrt0 + 1, 2)) 
    
    # [p0.remove(x) for x in p0 if x > 2 and x % 2 == 0]
    [p0.remove(x) for cp in range(3, limit+1, 2) if cp in p0 for x in p0 if x > cp and x % cp == 0 ]
    print(p0)

    last_found_prime = p0[-1]
    print(last_found_prime) # the last prime <= sqrt(limit)

    for icp, cp in enumerate(p0):
        if cp ** 2 > last_found_prime: # --> cp = the last prime <= sqrt(the last prime <= sqrt(limit))
                                        # <--> the last prime <= sqrt(sqrt(limit)) --> somewhere at approximately half-/mid-point of p0
            break

    # first_current_checked_sqrt_prime = cp
    current_checked_sqrt_prime_index = icp
    print(current_checked_sqrt_prime_index)

    p1 = []
    # x = last_found_prime

    for current_checked_sqrt_prime in p0[icp:]:
        if len(p1) > 0:
            last_found_prime = p1[-1]
            current_checked_sqrt_prime_index = current_checked_sqrt_prime_index + 1
        for x in range(last_found_prime + 2, (current_checked_sqrt_prime + 1) ** 2, 2):
            isPrime = True
            for current_checked_prime_index in range(current_checked_sqrt_prime_index + 1):
                if x % p0[current_checked_prime_index] == 0:
                    isPrime = False
                    break
            if isPrime:
                p1.append(x)
                # last_found_prime = x
                # break
                
    return p0 + p1

def prime(number):
    # when the prime function receives malformed input
    if number == None or number <= 0 or not str(number).isnumeric():
        raise ValueError('there is no zeroth prime')

    if number == 1:
        return 2
    if number == 2:
        return 3
    if number == 3:
        return 5
    
    logn = math.log(number) # ln (base e)
    # print(logn)  
    limit = int(number * logn * 1.2) + 100
    # print(limit)
    primes_list = primes(limit)
    # print(primes_list)

    return primes_list[number-1]