def governance_escalation(risk: float) -> str:
    if risk < 2:
        return "supervisor"
    elif risk < 4:
        return "compliance"
    elif risk < 7:
        return "audit"
    return "regulator"
