from dataclasses import dataclass


@dataclass
class Border:
    state1no: int
    state2no: int
    dyad: int
    state1ab: str
    state2ab: str
    year: int
    conttype: int
    version: int

    def __hash__(self):
        return hash((self.state1no, self.state2no))
    def __str__(self):
        return f"{self.state1ab}, {self.state2ab}"