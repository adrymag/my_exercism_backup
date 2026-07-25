# import math

def triplets_with_sum(number):
    pythagorean_triplets = []
    pythagorean_triplets_set = set()

    ''' say a <= b < c ; a ** 2 + b ** 2 = c ** 2 in [ 2 * a ** 2 ; 2 * b ** 2 ] <--> c ** 2  / 2 in [ a ** 2 ; b ** 2 ] <--> 2 in [(c/b)**2 ; (c/a)**2] <--> sqrt(2) in [ c/b ; c/a ] --> a + b + c = N in [ a * ( 2 + sqrt(2)) ; b * ( 2 + sqrt(2)) ] --> N / ( 2 + sqrt(2)) in [ a; b ] -->
    N (sqrt(2) - 1) / sqrt(2) in [ a; b ] <--> N - N/sqrt(2) in [ a; b ]
    '''

    '''
    a2 + b2 = c2, a+b+c=N, a <= b < c -> a2 + b2 = c2 in [ 2a2 ; 2b2 ] -> c2 / 2 in [a2 ; b2] -> c/s in [a;b] -> N in [a(2+s); b(2+s)] --> N/(2+s)     in [a;b]
    b + c = N - a in ( 2b ; 2c ) --> (N-a)/2 in (b; c)
    '''

    '''
    N2 = a2 + b2 + c2 + 2*S(ab) = 2(c2 + S(ab)) --> N2/2 = c2 + ab + c(a+b) --> 2 | N2 --> 2 | N
    '''

    '''

    a2 + b2 = c2 --> a = d (m2 - n2), b = d * 2mn, c = d(m2+n2), d | N, d = (a, b, c), (m, n) = 1 -> a + b + c = 2d (m2 + mn) = 2dm(m+n) ; m >= n >= 0 ; n = 0 -> b = 0 --> a2 = c2, N = 2a --> [0, N/2, N/2] ; d*m(m+n) = number/2 = N ; m > n > 0 --> m > n >= 1, m(m+n) >= 2(2+1) = 6

    m(m+n) in [2n2 ; 2m2] 

    number/2d = m(m+n) = div complem ai number/2d

    number = 2dm(m+n)    
    '''

    if number < 12 or number % 2 == 1:
        return []

    N = int(number / 2) # = dm(m+n)

    divisors = set()
    
    for d in range(1, N):
        if N % d == 0:
            divisors.add(d)

    # print(divisors)
    
    M = int(N/6)
    rm = set(range(M+1))
    divs = rm.intersection(divisors)
    # print(divs)

    for d in divs:
        # if N % d == 0:
        N2 = int(N / d)
        # print(d)
        # print(N2)
        # print([n for n in divisors if n <= N2 and N2 % n == 0])
        # print("********")
        for m in [m for m in divisors if m <= N2 and N2 % m == 0]: # range(int(sqrt(N2)) + 1):
            # if N2 % m == 0:
            p = int(N2 / m) # m + n
            if p > m and p < 2 * m:
                # print([n, p])
                n = p - m
                # print([m, n, p])
                if len([d for d in divisors if m % d == 0 and n % d == 0]) == 1: # (m, n) = 1
                    # print([m, n])
                    sqm = m ** 2
                    sqn = n ** 2
                    a = d * (sqm -sqn)
                    b = 2 * d * m * n
                    c = d * (sqm + sqn) # N - ( a + b )
                    # print([a, b, c])

                    current_set_len = len(pythagorean_triplets_set)

                    if a <= b:
                        pythagorean_triplets_set.add("*".join([str(a), str(b), str(c)]))
                        triplet = [a, b, c]
                    else:
                        pythagorean_triplets_set.add("*".join([str(b), str(a), str(c)]))
                        triplet = [b, a, c]

                    if len(pythagorean_triplets_set) > current_set_len:
                        current_set_len = len(pythagorean_triplets_set)
                        pythagorean_triplets.append(triplet)

    # m = int(number / (2 + math.sqrt(2)))
        
    # for a in range(m): # range(m):
    #     for b in range(a, int((number-a)/2)):
    #         c = number - (a + b)
    #         # if b ** 2 = (c + a)(c-a):
    #         if c ** 2 == a ** 2 + b ** 2:
    #             pythagorean_triplets.append((a, b, c))

    # for triplet in pythagorean_triplets_set:
        # pythagorean_triplets.append(triplet)
    
    return pythagorean_triplets # list(map(lambda x: int(x), list(pythagorean_triplets_set).split('*'))) # [s.split('*') for s in pythagorean_triplets_set] # [['3', '4', '5']] # list(pythagorean_triplets_set) # ['3*4*5']

print(triplets_with_sum(840))