from .enriched_category import EnrichedHom
from ..risk.risk_functor import risk_of_delta

def enriched_semantics(n1: int, n2: int) -> EnrichedHom:
    delta = n2 // n1
    risk = risk_of_delta(delta)
    return EnrichedHom(risk)
