from pairwise_memory.core.encoder import encode_state
from pairwise_memory.core.delta import compute_delta
from pairwise_memory.risk.risk_functor import risk_of_delta

n1 = encode_state({"actor": 1, "action": 2, "t": 1})
n2 = encode_state({"actor": 1, "action": 3, "t": 5})

d = compute_delta(n1, n2)
r = risk_of_delta(d)

print(n1, n2, d, r)
