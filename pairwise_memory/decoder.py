import sympy

def decode_state(encoded: int) -> dict:
    primes = list(sympy.primerange(2, 200))
    result = {}
    for p in primes:
        if encoded == 1:
            break
        exp = sympy.factorint(encoded).get(p, 0)
        result[p] = exp
    return result
