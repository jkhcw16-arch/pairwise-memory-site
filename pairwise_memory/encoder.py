import sympy

def encode_state(event: dict) -> int:
    primes = list(sympy.primerange(2, 200))
    encoded = 1
    for idx, (_, value) in enumerate(event.items()):
        encoded *= primes[idx] ** int(value)
    return encoded
