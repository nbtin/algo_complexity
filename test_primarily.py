import random
import math
from utils import *


# brute force from 2 to n - 1
def naive_1(n):
    comparisons = [0]
    if inc(comparisons) and n < 2:
        return False, comparisons[0]
    for i in range(2, n):
        if inc(comparisons) and n % i == 0:
            return False, comparisons[0]
    return True, comparisons[0]

# brute force from 2 to sqrt(n)
def naive_2(n):
    comparisons = [0]
    if inc(comparisons) and n < 2:
        return False, comparisons[0]
    for i in range(2, int(math.sqrt(n) + 1)):
        if inc(comparisons) and n % i == 0:
            return False, comparisons[0]
    return True, comparisons[0]

def fermat_little(n):
    comparisons = [0]
    # check the base cases
    if inc(comparisons) and n <= 1:
        return False, comparisons[0]
    elif inc(comparisons) and n <= 3:
        return True, comparisons[0]
    elif inc(comparisons) and n % 2 == 0:
        return False, comparisons[0]
    
    a = random.randint(2, n)
    _gcd, comp1 = gcd(a, n)
    _pow, comp2 = pow_(a, n - 1, n)

    comparisons[0] += comp1 # Phep so sanh cho if dau tien.

    if inc(comparisons) and _gcd != 1:
        return False, comparisons[0]
    elif inc(comparisons) and _pow != 1:
        comparisons[0] += comp2 
        return False, comparisons[0]
    else:
        comparisons[0] += comp2 
        return True, comparisons[0]


def miller_rabin_check(n, d, r):
    comparisons = [0]
    a = random.randint(2, n-2)
    x, comp = pow_(a, d, n)
    comparisons[0] += comp
    if (inc(comparisons) and x == 1) or (inc(comparisons) and x == n-1):
        return True, comparisons[0] # -> it's probably prime
    for _ in range(r-1):
        inc(comparisons)
        x, comp = pow_(x, 2, n)
        comparisons[0] += comp
        if inc(comparisons) and x == n-1:
            return True, comparisons[0] # -> it's probably prime
    else:
        inc(comparisons)
        return False, comparisons[0] # if it never equals to n - 1, it's a composite

def miller_rabin(n, k=5):
    """
    Miller-Rabin primality test.

    n: the number to be tested for primality
    k: the number of iterations to perform (default 5)

    Returns True if n is probably prime, False otherwise.
    """
    comparisons = [0]
    # check the base cases
    if inc(comparisons) and n <= 1:
        return False, comparisons[0]
    elif inc(comparisons) and n <= 3:
        return True, comparisons[0]
    elif inc(comparisons) and n % 2 == 0:
        return False, comparisons[0]

    # Write n-1 as d*2^r by factoring powers of 2 from n-1
    r = 0
    d = n - 1
    while inc(comparisons) and d % 2 == 0:
        r += 1
        d //= 2

    # Run Miller-Rabin k times
    for _ in range(k):
        inc(comparisons)        
        checker, comp = miller_rabin_check(n, d, r)
        comparisons[0] += comp
        if inc(comparisons) and checker:
            continue
        else:
            return False, comparisons[0]
        
    return True, comparisons[0]


if __name__ == '__main__':
    N = int(input("Input a number: "))
    print("PRIME") if miller_rabin(N)[0] else print("COMPOSITE")
    print("PRIME") if naive_2(N)[0] else print("COMPOSITE")
    print("PRIME") if fermat_little(N)[0] else print("COMPOSITE")
    # print("PRIME") if naive_1(N) else 
    # print("COMPOSITE") # CHAY CHAM VAI LON LUON :))
    