import chess


class MovementsTree:
    """
        Construct a tree with all of the legal moves on the board given in
        the constructor, the evalute fonction is executed on each node.
        The best node is kept.

        The depth attribute determines the number of legal moves
        to calculate in each position.

        The turn attribute determines which color has to play.

        White and black moves alternates between layers.
    """

    def __init__(self, board: chess.Board, depth: int):
        if depth < 0:
            raise Exception("Depth can't be negative")

        # Tree init
        self.tree = BoardNode(board)
        self.depth = depth

    # Trigger the tree building with all possibles moves within the depth
    def build(self):
        self.tree.build_children(self.depth)


class BoardNode:
    """
        Represent a node in a MovementsTree.
    """

    def __init__(self, board: chess.Board, lastMove: chess.Move):
        self.children = []
        self.board = board
        self.lastMove = lastMove

    def build_children(self, depth: int):
        """
            1. Choose the opponent best move with evaluation function
            2. Create all childs with all possible legal moves
        """
        if depth < 1:
            return
