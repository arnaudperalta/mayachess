import sys
import chess
from evaluation import find_best_move


def uci_handling():
    board = chess.Board()

    while True:
        msg = input()
        command(msg, board)


def command(msg: str, board: chess.Board):
    if msg == "quit":
        sys.exit()

    if msg == "uci":
        print("id name Maya Chess")
        print("id author Arnaud Peralta")
        print("uciok")

    if msg == "isready":
        print("readyok")

    if msg == "ucinewgame":
        return

    if "position startpos moves" in msg:
        moves = msg.split(' ')[3:]
        board.clear()
        board.set_fen(chess.STARTING_FEN)
        for move in moves:
            board.push(chess.Move.from_uci(move))
        return

    if "position fen" in msg:
        fen = " ".join(msg.split(" ")[2:])
        board.set_fen(fen)
        return

    if msg[0:2] == "go":
        move = find_best_move(board, 2)
        board.push(move)
        print(f'bestmove {move}')
        return
