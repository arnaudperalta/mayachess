import chess
from . import pieces_data as pdata


def evaluate_position(board: chess.Board) -> float:
    """Return a float representating the position in centipawns"""
    position = material_sum(board)
    position += material_position_bonus(board)
    return position


def evaluate_move(board: chess.Board, move: chess.Move) -> float:
    boardCopied = board.copy()
    boardCopied.push(move)
    return evaluate_position(boardCopied)


def material_sum(board: chess.Board) -> float:
    """
        Return a float representating the sums of every chess pieces
        on the board for each side with a final substraction.
    """
    position = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        # Here, the move is already played
        if piece.color == chess.BLACK:
            position += pdata.piece_values[piece.piece_type]
        else:
            position -= pdata.piece_values[piece.piece_type]
    return position


def material_position_bonus(board: chess.Board) -> float:
    """
        Return a value for each pieces from the data arrays located in
        pieces_data.py.
        These value are summed into a position value added to the evaluation.
    """
    position = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        # If the turn is black, substract by 64 - 1 for reversing the board
        # The move is already played so we check if the turn is for white
        if board.turn == chess.WHITE:
            square = 63 - square
        if piece.piece_type == chess.PAWN:
            position += pdata.pawn_table[square]
        elif piece.piece_type == chess.KNIGHT:
            position += pdata.knight_table[square]
        elif piece.piece_type == chess.BISHOP:
            position += pdata.bishop_table[square]
        elif piece.piece_type == chess.ROOK:
            position += pdata.rook_table[square]
        elif piece.piece_type == chess.QUEEN:
            position += pdata.queen_table[square]
        elif piece.piece_type == chess.KING:
            position += pdata.king_middle_game_table[square]
        # TODO : add king late game table
    if board.turn == chess.WHITE:
        position *= -1
    return position


def find_best_move(board: chess.Board) -> chess.Move:
    # Browsing all legal moves
    bestValue = None
    bestMove = None
    for move in board.legal_moves:
        # Evaluating the position for each moves
        positionValue = evaluate_move(board, move)
        if bestValue is None:
            bestValue = positionValue
            bestMove = move
        elif board.turn == chess.WHITE and bestValue < positionValue:
            bestValue = positionValue
            bestMove = move
        elif board.turn == chess.BLACK and bestValue > positionValue:
            bestValue = positionValue
            bestMove = move
    return bestMove
