from .enriched_semantics import enriched_semantics
from ..risk.governance_escalation import governance_escalation

def enriched_escalation(n1: int, n2: int) -> str:
    enriched = enriched_semantics(n1, n2)
    return governance_escalation(enriched.value)
