def risk_of_delta(delta: int) -> float:
    # Risk = sum of exponents
    import sympy
    factors = sympy.factorint(delta)
    return float(sum(factors.values()))
