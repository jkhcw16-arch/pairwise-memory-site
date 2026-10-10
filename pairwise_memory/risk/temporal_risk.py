def risk_trajectory(states: list[int]) -> list[float]:
    risks = []
    for i in range(len(states) - 1):
        d = states[i+1] // states[i]
        risks.append(risk_of_delta(d))
    return risks
