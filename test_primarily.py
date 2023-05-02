import random
import math
from utils import *

# brute force from 2 to n - 1
def naive_1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# brute force from 2 to sqrt(n)
def naive_2(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def fermat_little(n):
    a = random.randint(2, n)
    if gcd(a, n) != 1:
        return False
    elif pow(a, n - 1, n) != 1:
        return False
    else:
        return True


def miller_rabin_check(n, d, r):
    a = random.randint(2, n-2)
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True # -> it's probably prime
    for _ in range(r-1):
        x = pow(x, 2, n)
        if x == n-1:
            return True # -> it's probably prime
    else:
        return False # if it never equals to n - 1, it's a composite

def miller_rabin(n, k=5):
    """
    Miller-Rabin primality test.

    n: the number to be tested for primality
    k: the number of iterations to perform (default 5)

    Returns True if n is probably prime, False otherwise.
    """

    # check the base cases
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    # Write n-1 as d*2^r by factoring powers of 2 from n-1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Run Miller-Rabin k times
    for _ in range(k):
        """ All-in-one function """
        # a = random.randint(2, n-2)
        # x = pow(a, d, n)
        # if x == 1 or x == n-1:
        #     continue # -> it's probably prime
        # for _ in range(r-1):
        #     x = pow(x, 2, n)
        #     if x == n-1:
        #         break # -> it's probably prime
        # else:
        #     return False # if it never equals to n - 1, it's a composite
        
        """ Call miller_rabin_check() for ease of understanding <(") """
        checker = miller_rabin_check(n, d, r)
        if checker:
            continue
        else:
            return False
        
    return True


if __name__ == '__main__':
    N = int(input("Input a number: "))
    print("PRIME") if miller_rabin(N) else print("COMPOSITE")
    print("PRIME") if naive_2(N) else print("COMPOSITE")
    print("PRIME") if fermat_little(N) else print("COMPOSITE")
    # print("PRIME") if naive_1(N) else print("COMPOSITE") # CHAY CHAM VAI LON LUON :))
    