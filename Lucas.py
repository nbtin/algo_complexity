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


def Check_Perfect_Sqr(n : int):
    low = 1
    high = x
    while (low <= high):
        mid = (low + high) // 2
        if mid * mid < n :
            low = low + 1
        elif mid * mid > n:
            high = mid - 1
        else:
            return True
    return False

def get_UV(n: int, P: int, Q: int, D: int):
    U = 1
    V = P
    Q_k = Q
    n -= 1
    while n:
        U_new = U * V
        V_new = V**2 - 2*Q_k
        Q_k = Q_k * Q_k
        
        if (n & 1):
            U = (P*U_new + V_new) 
            V = (D*U_new + P*V_new)
            if U & 1:
                U += n
            if V & 1:
                V += n
            U >>= 1
            V >>= 1
            Q_k *= Q
        else:
            U, V = U_new, V_new
        n >>= 1
    return U, V

def Strong_Lucas_propable_prime(n):
    pass
