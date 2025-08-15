from dataclasses import dataclass

@dataclass
class Piece:
    color: str
    type: str
    is_dead: bool = False
    has_moved: bool = False
    position: list[int,int]
    available_moves: list[list[int,int]] = []

#initialize all pieces on the board
def initialize_pieces(color: str):
  if color == "white":
    piece_rank = 0
    pawn_rank = 1
  elif color == "black":
    piece_rank = 7
    pawn_rank = 6

  pieces = list[Piece]    
  
  pieces.append(Piece(color=color, type="R", has_moved=False, position=[piece_rank, 0], available_moves=[]))
  pieces.append(Piece(color=color, type="N", has_moved=False, position=[piece_rank, 1], available_moves=[]))
  pieces.append(Piece(color=color, type="B", has_moved=False, position=[piece_rank, 2], available_moves=[]))
  pieces.append(Piece(color=color, type="Q", has_moved=False, position=[piece_rank, 3], available_moves=[]))
  pieces.append(Piece(color=color, type="K", has_moved=False, position=[piece_rank, 4], available_moves=[]))
  pieces.append(Piece(color=color, type="B", has_moved=False, position=[piece_rank, 5], available_moves=[]))
  pieces.append(Piece(color=color, type="N", has_moved=False, position=[piece_rank, 6], available_moves=[]))
  pieces.append(Piece(color=color, type="R", has_moved=False, position=[piece_rank, 7], available_moves=[]))

  for pawn_file in range(8):
    pieces.append(Piece(color, "P", False, [pawn_rank, pawn_file], []))

  return pieces
