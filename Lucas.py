from utils import gcd
from test_primarily import naive_2, miller_rabin
from utils import *

## Thư viện dùng cho việc kiểm tra lại hàm
from sympy.ntheory import jacobi_symbol 

def Jacobi(a: int, n: int):  
    """
    Nguồn: https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_C++
    """
    comparisons = [0]
    assert (n > 0) and (n & 1)
    a = a % n
    t = 1
    r = None  # Khởi tạo r
    while inc(comparisons) and a:  # a != 0
        while inc(comparisons) and not (a & 1):  # a % 2 == 0
            a >>= 1
            r = n & 7  # n % (8) == n & 7
            if inc(comparisons) and (r in [3, 5]):
                t = -t
        r = n
        n = a
        a = r
        if inc(comparisons) and (a & 3) == 3 and inc(comparisons) and (n & 3) == 3:
            t = -t
        a = a % n
    if inc(comparisons) and (n == 1):
        return t, comparisons[0]
    return 0, comparisons[0]


def find_DPQ(n):
    comparisons = [0]
    D = 5
    while inc(comparisons) and True:
        g, comp = gcd(abs(D), n)
        comparisons[0] += comp
        if inc(comparisons) and 1 < g and inc(comparisons) and g < n:
            return (0, 0, 0), comparisons[0]
        jacobi, comp = Jacobi(D, n)
        comparisons[0] += comp
        if inc(comparisons) and jacobi == -1:
            break
        
        if inc(comparisons) and D > 0:
            D = -D - 2
        else:
            D = -D + 2
            
    assert Jacobi(D, n)[0] == jacobi_symbol(D, n)
    assert (1 - D) % 4 == 0 
    P = 1
    Q = (1 - D) // 4
    return (D, P, Q), comparisons[0]


def Check_Perfect_Sqr(n: int):
    """Kiểm tra một số nguyên có phải là số chính phương hay không

    Args:
        n (int): số cần kiểm tra 

    Returns:
        Boolean: True nếu nó là số chính phương
    """
    comparisons = [0]
    low = 1
    high = n
    while inc(comparisons) and (low <= high):
        mid = (low + high) >> 1
        number = mid * mid
        if inc(comparisons) and number < n:
            low = low + 1  
        elif inc(comparisons) and number > n:
            high = mid - 1
        else:
            return True, comparisons[0]
    return False, comparisons[0]


def find_UVQ(n: int, P: int, Q: int, k: int):
    comparisons = [0]
    D = P*P - 4*Q
    if inc(comparisons) and k == 0:
        return (0, 2, Q), comparisons[0]
    U = 1
    V = P
    Qk = Q
    b = 0
    temp = k
    while inc(comparisons) and temp:
        temp >>= 1
        b += 1
    
    while b > 1:
        U = (U*V) % n
        V = (V*V - 2*Qk) % n
        Qk = (Qk * Qk) %n 
        b -= 1
        if inc(comparisons) and ((k >> (b - 1)) & 1):
            U, V = U*P + V, V*P + U*D
            if inc(comparisons) and (U & 1):
                U += n
            if inc(comparisons) and (V & 1):
                V += n
            U, V = U >> 1, V >> 1
            Qk *= Q
        Qk %= n
    return (U % n, V % n, Qk), comparisons[0]

    

##TODO nhớ xóa assert sau khi chạy

def Strong_Lucas_propable_prime(n):
    comparisons = [0]

    ## Xử lý tiền tố các trường hợp cơ bản
    if inc(comparisons) and n == 2:
        return True, comparisons[0]
    if inc(comparisons) and (n < 2 or (n & 1) == 0):
        return False, comparisons[0]
    checker, comp = Check_Perfect_Sqr(n)
    comparisons[0] += comp
    if inc(comparisons) and checker:
        return False, comparisons[0]
    
    (D, P, Q), comp = find_DPQ(n)
    comparisons[0] += comp
    if inc(comparisons) and D == 0:
        return False, comparisons[0]   
     
    k = n + 1
    s = 0
    while inc(comparisons) and not (k & 1):
        k >>= 1
        s += 1
    
    (U, V, Qk), comp = find_UVQ(n, P, Q, k)
    comparisons[0] += comp
    
    if (inc(comparisons) and (U == 0)) or (inc(comparisons) and (V == 0)):
        return True, comparisons[0]
    
    for r in range(1, s):
        V = (V*V - 2*Qk) % n
        if inc(comparisons) and (V == 0):
            return True, comparisons[0]
        Qk, comp = pow_(Qk, 2, n)
        comparisons[0] += comp

    return False, comparisons[0]
    



## Các thông số được lấy từ github của sympy về Baillie-PSW test
_LIMIT = 10000 # cái ngưỡng để kiểm tra số nguyên tố bằng thuật toán Naive 
LOW_PRIMES = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def Baillie_PSW_Test(n):
    comparisons = [0]
    if (inc(comparisons)) and (n == 2):
        return True, comparisons[0]
    
    if (inc(comparisons) and n < 2) or (inc(comparisons) and not (n & 1)): 
        return False, comparisons[0]

    if (inc(comparisons)) and (n <= _LIMIT):
        naive2, comp = naive_2(n)
        comparisons[0] += comp
        return naive2, comparisons[0]

    for i in LOW_PRIMES:  # kiểm tra có ước nguyên tố là các nguyên tố nhỏ không
        if (inc(comparisons)) and (n % i == 0):
            return False, comparisons[0]

    ## Sau khi kiểm tra xong thì chúng ta sẽ thực hiện 2 test chính
    # Miller - Rabin với base 2

    result, comp = miller_rabin(n, 1, True)
    comparisons[0] += comp
    if (inc(comparisons)) and (not result):
        return False, comparisons[0]

    
    # Lucas strong Propable prime test
    result, comp = Strong_Lucas_propable_prime(n)
    comparisons[0] += comp
    return result, comparisons[0]

print(Baillie_PSW_Test(67601)[0])