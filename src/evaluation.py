import chess
from pieces_data import get_piece_table, get_piece_value


def evaluate_position(board: chess.Board) -> float:
    """Return a float representating the position in centipawns"""
    position = material_sum(board)
    return position


def material_sum(board: chess.Board) -> float:
    """
        Return a float representating the sums of every chess pieces
        on the board for each side with a final substraction.
        We add the position values from material_position_bonus.
    """
    position = 0
    is_endgame = check_end_game(board)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        # Here, the move is already played
        if piece.color == chess.WHITE:
            position += get_piece_value(piece.piece_type)
            position += material_position_bonus(square, piece.piece_type,
                                                chess.WHITE, is_endgame)
        else:
            position -= get_piece_value(piece.piece_type)
            position -= material_position_bonus(square, piece.piece_type,
                                                chess.BLACK, is_endgame)
    return position


def material_position_bonus(square: int, piece_type: chess.Piece,
                            color: bool, endgame: bool = False) -> float:
    # If the turn is black, substract by 64 - 1 for reversing the board
    # The move is already played so we check if the turn is for white
    if color == chess.BLACK:
        square = 63 - square
    if piece_type == chess.PAWN:
        table = get_piece_table(chess.PAWN)
    elif piece_type == chess.KNIGHT:
        table = get_piece_table(chess.KNIGHT)
    elif piece_type == chess.BISHOP:
        table = get_piece_table(chess.BISHOP)
    elif piece_type == chess.ROOK:
        table = get_piece_table(chess.ROOK)
    elif piece_type == chess.QUEEN:
        table = get_piece_table(chess.QUEEN)
    else:
        table = get_piece_table(chess.KING, endgame)
    return table[square]


def find_best_move(board: chess.Board, depth: int) -> chess.Move:
    # Browsing all legal moves
    bestValue = None
    bestMove = None
    bestDepth = None
    for move in board.legal_moves:
        board.push(move)
        # Evaluating the position for each moves
        (positionValue, d) = minimax(board, depth, depth, -float("inf"),
                                     float("inf"), board.turn)
        board.pop()
        if positionValue == -float("inf") or positionValue == float("inf"):
            if bestDepth is None or d < bestDepth:
                print(d)
                bestDepth = d
                bestValue = positionValue
                bestMove = move
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


def check_end_game(board: chess.Board):
    queens = 0
    minors_pieces = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (piece.piece_type == chess.BISHOP
                      or piece.piece_type == chess.KNIGHT):
            minors_pieces += 1

    if queens == 0 or (queens == 2 and minors_pieces <= 1):
        return True

    return False


def minimax(board: chess.Board, originalDepth: int, depth, alpha,
            beta: float, maximizingPlayer: bool):
    """
        Minimax algorithm returning a tuple in case of checkmate
        We want to checkmate the fastest way, so we just need to compare
        the depth where the algorithm returned the tuple.

        originalDepth permits to calculate the difference between the actuel
        depth and the orignal depth of the tree. We can calulcate the shortest
        checkmate for example
    """
    # Returning -inf for white because this turn
    # has not been played
    if board.is_checkmate():
        if maximizingPlayer == chess.WHITE:
            return (-float('inf'), originalDepth - depth)
        else:
            return (float('inf'), originalDepth - depth)
    elif board.is_game_over():
        return (0, originalDepth - depth)

    if depth == 0:
        return (evaluate_position(board), originalDepth - depth)

    if maximizingPlayer == chess.WHITE:
        maxEval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            (value, _) = minimax(board, originalDepth, depth - 1,
                                 alpha, beta, chess.BLACK)
            board.pop()
            maxEval = max(maxEval, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return (maxEval, depth)
    else:
        minEval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            (value, _) = minimax(board, originalDepth, depth - 1,
                                 alpha, beta, chess.WHITE)
            board.pop()
            minEval = min(minEval, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return (minEval, depth)
