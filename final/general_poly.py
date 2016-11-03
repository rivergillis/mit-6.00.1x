def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    general_poly([1,2,3,4])(10) = 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0 = 1234
    """
    def poly(x):
        total = 0
        for i in range(len(L)):
            total += L[i] * (x)**(len(L) - 1 - i)
        return total
    return poly

print(general_poly([1,2,3,4])(10))
