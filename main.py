from dataclasses import dataclass, field

@dataclass
class Piece:
    color: str
    type: str
    position: list[int]
    available_moves: list[list[int]] = field(default_factory=list)
    has_moved: bool = False
    is_dead: bool = False

#initialize all pieces on the board
def initialize_pieces():
  pieces: list[Piece] = []
  
  for color in ["white", "black"]:
    piece_rank = 0 if color == "white" else 7
    pawn_rank = 1 if color == "white" else 6

    pieces.append(Piece(color=color, type="R", position=[piece_rank, 0]))
    pieces.append(Piece(color=color, type="N", position=[piece_rank, 1]))
    pieces.append(Piece(color=color, type="B", position=[piece_rank, 2]))
    pieces.append(Piece(color=color, type="Q", position=[piece_rank, 3]))
    pieces.append(Piece(color=color, type="K", position=[piece_rank, 4]))
    pieces.append(Piece(color=color, type="B", position=[piece_rank, 5]))
    pieces.append(Piece(color=color, type="N", position=[piece_rank, 6]))
    pieces.append(Piece(color=color, type="R", position=[piece_rank, 7]))

    for pawn_file in range(8):
      pieces.append(Piece(color=color, type="P", position=[pawn_rank, pawn_file]))

  return pieces