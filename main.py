from Design_Patterns.Structural_Patterns.Adapter.RoundHole import RoundHole
from Design_Patterns.Structural_Patterns.Adapter.RoundPeg import RoundPeg
from Design_Patterns.Structural_Patterns.Adapter.SquarePeg import SquarePeg
from Design_Patterns.Structural_Patterns.Adapter.SquarePegAdapter import SquarePegAdapter

if __name__ == "__main__":
    round_hole = RoundHole(5)

    round_peg = RoundPeg(4)
    print(round_hole.fits(round_peg))

    square_round_peg = SquarePegAdapter(SquarePeg(12))
    print(round_hole.fits(square_round_peg))
