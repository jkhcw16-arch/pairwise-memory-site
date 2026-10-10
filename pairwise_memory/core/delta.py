def compute_delta(n1: int, n2: int) -> int:
    if n1 == 0:
        raise ValueError("State cannot be zero.")
    return n2 // n1
