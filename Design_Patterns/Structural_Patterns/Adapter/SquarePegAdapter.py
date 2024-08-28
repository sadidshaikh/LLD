from Design_Patterns.Structural_Patterns.Adapter.RoundPeg import RoundPeg
from Design_Patterns.Structural_Patterns.Adapter.SquarePeg import SquarePeg


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg):
        self.peg = peg
        super().__init__(self.get_radius())

    def get_radius(self) -> int:
        return int(self.peg.get_width() / 2)
