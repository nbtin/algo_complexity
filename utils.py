
def inc(x):
    x[0] = x[0] + 1
    return True

def gcd(a, b):
    comparisons = [0]
    while inc(comparisons) and b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a, comparisons[0]

def pow_(a, b, c):
    """Implement the pow function using the Binary Exponentiation trick to get the complexity of log(b).
    References: https://cp-algorithms.com/algebra/binary-exp.html
    """
    comparisons = [0]
    result = 1
    a = a % c

    while inc(comparisons) and b > 0:
        if inc(comparisons) and b & 1:
            result = (result * a) % c
        b >>= 1
        a = (a * a) % c

    return result, comparisons[0]