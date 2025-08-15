from dataclasses import dataclass

@dataclass
class Piece:
    color: str
    type: str
    has_moved: bool
    position: []
    available_moves: []