import chess

# Datas from https://www.chessprogramming.org/Simplified_Evaluation_Function


def get_piece_value(piece_type: chess.PieceType) -> float:
    if piece_type == chess.PAWN:
        return 1.00
    if piece_type == chess.ROOK:
        return 5.00
    if piece_type == chess.KNIGHT:
        return 3.20
    if piece_type == chess.BISHOP:
        return 3.30
    if piece_type == chess.QUEEN:
        return 9.00
    if piece_type == chess.KING:
        return 200.00


"""
Tables are represented like the chess package board representation :
A1, B1, C1, D1, E1, F1, G1, H1,
A2, B2, C2, D2, E2, F2, G2, H2,
...

These datas are for white side only, for black use a position modification
is needed.
Exemple : H8 is 63 in the chess lib, the correct position for these datas is
63 - H8 = A1 = 0; 63 - H2 = A7 = 48
"""


def get_piece_table(piece_type: chess.PieceType, endgame: bool = False):
    if piece_type == chess.PAWN:
        return [
            0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, 0.00,
            0.05,  0.10,  0.10, -0.20, -0.20,  0.10,  0.10, 0.05,
            0.05, -0.05, -0.10,  0.00,  0.00, -0.10, -0.05, 0.05,
            0.00,  0.00,  0.00,  0.20,  0.20,  0.00,  0.00, 0.00,
            0.05,  0.05,  0.10,  0.25,  0.25,  0.10,  0.05, 0.05,
            0.10,  0.10,  0.20,  0.30,  0.30,  0.20,  0.10, 0.10,
            0.50,  0.50,  0.50,  0.50,  0.50,  0.50,  0.50, 0.50,
            0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, 0.00
        ]
    if piece_type == chess.ROOK:
        return [
            0.00,  0.00, 0.00, 0.05, 0.05, 0.00, 0.00,  0.00,
            -0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.05,
            -0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.05,
            -0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.05,
            -0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.05,
            -0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.05,
            0.05,  0.10, 0.10, 0.10, 0.10, 0.10, 0.10,  0.05,
            0.00,  0.00, 0.00, 0.00, 0.00, 0.00, 0.00,  0.00
        ]
    if piece_type == chess.KNIGHT:
        return [
            -0.50, -0.40, -0.30, -0.30, -0.30, -0.30, -0.40, -0.50,
            -0.40, -0.20,  0.00,  0.05,  0.05,  0.00, -0.20, -0.40,
            -0.30,  0.05,  0.10,  0.15,  0.15,  0.10,  0.05, -0.30,
            -0.30,  0.00,  0.15,  0.20,  0.20,  0.15,  0.00, -0.30,
            -0.30,  0.05,  0.15,  0.20,  0.20,  0.15,  0.05, -0.30,
            -0.30,  0.00,  0.10,  0.15,  0.15,  0.10,  0.00, -0.30,
            -0.40, -0.20,  0.00,  0.00,  0.00,  0.00, -0.20, -0.40,
            -0.50, -0.40, -0.30, -0.30, -0.30, -0.30, -0.40, -0.50
        ]
    if piece_type == chess.BISHOP:
        return [
            -0.20, -0.10, -0.10, -0.10, -0.10, -0.10, -0.10, -0.20,
            -0.10,  0.05,  0.00,  0.00,  0.00,  0.00,  0.05, -0.10,
            -0.10,  0.10,  0.10,  0.10,  0.10,  0.10,  0.10, -0.10,
            -0.10,  0.00,  0.10,  0.10,  0.10,  0.10,  0.00, -0.10,
            -0.10,  0.05,  0.05,  0.10,  0.10,  0.05,  0.05, -0.10,
            -0.10,  0.00,  0.05,  0.10,  0.10,  0.05,  0.00, -0.10,
            -0.10,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.10,
            -0.20, -0.10, -0.10, -0.10, -0.10, -0.10, -0.10, -0.20
        ]
    if piece_type == chess.QUEEN:
        return [
            -0.20, -0.10, -0.10, -0.05, -0.05, -0.10, -0.10, -0.20,
            -0.10,  0.00,  0.05,  0.00,  0.00,  0.00,  0.00, -0.10,
            -0.10,  0.05,  0.05,  0.05,  0.05,  0.05,  0.00, -0.10,
            0.00,   0.00,  0.05,  0.05,  0.05,  0.05,  0.00, -0.05,
            -0.05,  0.00,  0.05,  0.05,  0.05,  0.05,  0.00, -0.05,
            -0.10,  0.00,  0.05,  0.05,  0.05,  0.05,  0.00, -0.10,
            -0.10,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.10,
            -0.20, -0.10, -0.10, -0.05, -0.05, -0.10, -0.10, -0.20
        ]
    if piece_type == chess.KING and not endgame:
        return [
            0.20,   0.30,  0.10,  0.00,  0.00,  0.10,  0.30,  0.20,
            0.20,   0.20,  0.00,  0.00,  0.00,  0.00,  0.20,  0.20,
            -0.10, -0.20, -0.20, -0.20, -0.20, -0.20, -0.20, -0.10,
            -0.20, -0.30, -0.30, -0.40, -0.40, -0.30, -0.30, -0.20,
            -0.30, -0.40, -0.40, -0.50, -0.50, -0.40, -0.40, -0.30,
            -0.30, -0.40, -0.40, -0.50, -0.50, -0.40, -0.40, -0.30,
            -0.30, -0.40, -0.40, -0.50, -0.50, -0.40, -0.40, -0.30,
            -0.30, -0.40, -0.40, -0.50, -0.50, -0.40, -0.40, -0.30
        ]
    if piece_type == chess.KING and endgame:
        return [
            -0.50, -0.30, -0.30, -0.30, -0.30, -0.30, -0.30, -0.50,
            -0.30, -0.30,  0.00,  0.00,  0.00,  0.00, -0.30, -0.30,
            -0.30, -0.10,  0.20,  0.30,  0.30,  0.20, -0.10, -0.30,
            -0.30, -0.10,  0.30,  0.40,  0.40,  0.30, -0.10, -0.30,
            -0.30, -0.10,  0.30,  0.40,  0.40,  0.30, -0.10, -0.30,
            -0.30, -0.10,  0.20,  0.30,  0.30,  0.20, -0.10, -0.30,
            -0.30, -0.20, -0.10,  0.00,  0.00, -0.10, -0.20, -0.30,
            -0.50, -0.40, -0.30, -0.20, -0.20, -0.30, -0.40, -0.50
        ]
