class EnrichedHom:
    def __init__(self, value):
        self.value = value

    def combine(self, other):
        return EnrichedHom(self.value + other.value)
