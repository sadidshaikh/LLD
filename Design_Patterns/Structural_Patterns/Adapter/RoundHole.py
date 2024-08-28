from Design_Patterns.Structural_Patterns.Adapter.RoundPeg import RoundPeg


class RoundHole:
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self) -> int:
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()
