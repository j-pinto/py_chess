from dataclasses import dataclass

@dataclass
class Piece:
    color: str
    type: str
    has_moved: bool
    position: list[int,int]
    available_moves: list[list[int,int]]

#initialize all pieces on the board
def initialize_pieces(color):
  if color == "white":
    piece_rank = 0
    pawn_rank = 1
  elif color == "black":
    piece_rank = 7
    pawn_rank = 6

  pieces = []    
  
  pieces.append(Piece(color, "R", False, [piece_rank, 0], []))
  pieces.append(Piece(color, "N", False, [piece_rank, 1], []))
  pieces.append(Piece(color, "B", False, [piece_rank, 2], []))
  pieces.append(Piece(color, "Q", False, [piece_rank, 3], []))
  pieces.append(Piece(color, "K", False, [piece_rank, 4], []))
  pieces.append(Piece(color, "B", False, [piece_rank, 5], []))
  pieces.append(Piece(color, "N", False, [piece_rank, 6], []))
  pieces.append(Piece(color, "R", False, [piece_rank, 7], []))

  for pawn_file in range(8):
    pieces.append(Piece(color, "P", False, [pawn_rank, pawn_file], []))

  return pieces
