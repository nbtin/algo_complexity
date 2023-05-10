from utils import gcd
from test_primarily import naive_2, miller_rabin
def Jacobi(a: int, n: int):  # Nguồn: https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_C++
    assert (n > 0) and (n & 1)
    a = a % n
    t = 1
    r = None  # Khởi tạo r
    while a:  # a != 0
        while not (a & 1):  # a % 2 == 0
            a >>= 1
            r = n & 7  # n % (8) == n & 7
            if r in [3, 5]:
                t = -t
        r = n
        n = a
        a = r
        if (a & 3) == 3 and (n & 3) == 3:
            t = -t
        a = a % n
    if (n == 1):
        return t
    return 0


def find_DPQ(n):
    D = 5
    while True:
        g = gcd(abs(d), n)
        if 1 < g and g < n:
            return (0, 0, 0)
        if Jacobi(d, n) != -1:
            d = -(d + (d // (abs(d))) * 2)
        break
    assert Jacobi(d, n) == jacobi_symbol(d, n)
    assert (1 - d) % 4 == 0 
    P = 1
    Q = (1 - D) // 4
    return (D, P, Q)


def Check_Perfect_Sqr(n: int):
    """Kiểm tra một số nguyên có phải là số chính phương hay không

    Args:
        n (int): số cần kiểm tra 

    Returns:
        Boolean: True nếu nó là số chính phương
    """
    low = 1
    high = x
    while (low <= high):
        mid = (low + high) >> 1
        number = mid * mid
        if number < n:
            low = low + 1  
        elif number > n:
            high = mid - 1
        else:
            return True
    return False


def find_UVQ(n: int, P: int, Q: int, k: int):
    D = P*P - 4*Q
    if k == 0:
        return (0, 2, Q)
    U = 1
    V = P
    Qk = Q
    
    pass

##TODO nhớ xóa assert sau khi chạy

def Strong_Lucas_propable_prime(n):
    ## Xử lý tiền tố các trường hợp cơ bản
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    if Check_Perfect_Sqr(n):
        return False
    
    D, P, Q = find_DPQ(n)
    if D == 0:
        return False    
    k = n + 1
    s = 0
    while not (k & 1):
        k >>= 1
        s += 1
    
    U, V, Qk = find_UVQ(n, P, Q, k)
    
    
    pass


from  sympy.ntheory import jacobi_symbol

Strong_Lucas_propable_prime(19)

## Các thông số được lấy từ github của sympy về Baillie-PSW test
_LIMIT = 10000 # cái ngưỡng để kiểm tra số nguyên tố bằng thuật toán Naive 
LOW_PRIMES = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def Baillie_PSW_Test(n):
    if n < 2 or not (n & 1): return False
    if n == 2: return True
    if n <= _LIMIT:
        return naive_2(n)
    
    for i in LOW_PRIMES:
        if n % i == 0:
            return False
        
    ## Sau khi kiểm tra xong thì chúng ta sẽ thực hiện 2 test chính
    # Miller - Rabin với base 2
    
    # Lucas strong Propable prime test

                    


