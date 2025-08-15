from dataclasses import dataclass

@dataclass
class Piece:
    color: str
    type: str
    has_moved: bool
    position: []
    available_moves: []

#initialize all pieces on the board
def initialize_pieces():
    white_king = Piece("white", "king", False, [0, 4], [])
    white_queen = Piece("white", "queen", False, [0, 3], [])
    white_bishop1 = Piece("white", "bishop", False, [0, 2], [])
    white_bishop2 = Piece("white", "bishop", False, [0, 5], [])
    white_knight1 = Piece("white", "knight", False, [0, 1], [])
    white_knight2 = Piece("white", "knight", False, [0, 6], [])
    white_rook1 = Piece("white", "rook", False, [0, 0], [])
    white_rook2 = Piece("white", "rook", False, [0, 7], [])
    white_pawn1 = Piece("white", "pawn", False, [1, 0], [])
    white_pawn2 = Piece("white", "pawn", False, [1, 1], [])
    white_pawn3 = Piece("white", "pawn", False, [1, 2], [])
    white_pawn4 = Piece("white", "pawn", False, [1, 3], [])
    white_pawn5 = Piece("white", "pawn", False, [1, 4], [])
    white_pawn6 = Piece("white", "pawn", False, [1, 5], [])
    white_pawn7 = Piece("white", "pawn", False, [1, 6], [])
    white_pawn8 = Piece("white", "pawn", False, [1, 7], [])

    black_king = Piece("black", "king", False, [7, 4], [])
    black_queen = Piece("black", "queen", False, [7, 3], [])
    black_bishop1 = Piece("black", "bishop", False, [7, 2], [])
    black_bishop2 = Piece("black", "bishop", False, [7, 5], [])
    black_knight1 = Piece("black", "knight", False, [7, 1], [])
    black_knight2 = Piece("black", "knight", False, [7, 6], [])
    black_rook1 = Piece("black", "rook", False, [7, 0], [])
    black_rook2 = Piece("black", "rook", False, [7, 7], [])
    black_pawn1 = Piece("black", "pawn", False, [6, 0], [])
    black_pawn2 = Piece("black", "pawn", False, [6, 1], [])
    black_pawn3 = Piece("black", "pawn", False, [6, 2], [])
    black_pawn4 = Piece("black", "pawn", False, [6, 3], [])
    black_pawn5 = Piece("black", "pawn", False, [6, 4], [])
    black_pawn6 = Piece("black", "pawn", False, [6, 5], [])
    black_pawn7 = Piece("black", "pawn", False, [6, 6], [])
    black_pawn8 = Piece("black", "pawn", False, [6, 7], [])

    return
