package main

import (
	"math"

	"github.com/notnil/chess"
)

type minimax_res struct {
	evaluation float64
	depth      int
}

func Find_best_move(game *chess.Game, depth int) *chess.Move {
	var best_is_found = false
	var best_eval = 0.0
	var best_move *chess.Move
	var best_depth = 0
	for _, move := range game.ValidMoves() {
		var clone = game.Clone()
		clone.Move(move)
		var eval = minimax(clone, depth, depth, math.Inf(-1),
			math.Inf(1), game.Position().Turn())
		// Found checkmate in game tree
		if eval.evaluation == math.Inf(-1) || eval.evaluation == math.Inf(1) {
			if best_depth == 0 || eval.depth < best_depth {
				best_depth = eval.depth
				best_eval = eval.evaluation
				best_move = move
				best_is_found = true
			}
		}
		if !best_is_found {
			best_eval = eval.evaluation
			best_move = move
			best_is_found = true
		} else if (game.Position().Turn() == chess.White && best_eval < eval.evaluation) ||
			(game.Position().Turn() == chess.Black && best_eval > eval.evaluation) {
			best_eval = eval.evaluation
			best_move = move
		}
	}
	return best_move
}

func minimax(game *chess.Game, originDepth int, depth int, alpha float64,
	beta float64, color chess.Color) minimax_res {

	if game.Method() == chess.Checkmate {
		if color == chess.White {
			return minimax_res{math.Inf(-1), originDepth - depth}
		}
		return minimax_res{math.Inf(1), originDepth - depth}
	} else if game.Method() != chess.NoMethod { // Game is over but not by checkmate
		return minimax_res{0, originDepth - depth}
	}

	if depth == 0 {
		return minimax_res{EvaluateGame(game), originDepth - depth}
	}

	if color == chess.White {
		var best_eval = math.Inf(-1)
		for _, move := range game.ValidMoves() {
			var clone = game.Clone()
			clone.Move(move)
			var eval = minimax(game, originDepth, depth-1,
				alpha, beta, chess.Black)
			best_eval = math.Max(best_eval, eval.evaluation)
			if alpha >= beta {
				return minimax_res{best_eval, depth}
			}
		}
		return minimax_res{best_eval, depth}
	} else {
		var best_eval = math.Inf(1)
		for _, move := range game.ValidMoves() {
			var clone = game.Clone()
			clone.Move(move)
			var eval = minimax(game, originDepth, depth-1,
				alpha, beta, chess.White)
			best_eval = math.Min(best_eval, eval.evaluation)
			if alpha >= beta {
				return minimax_res{best_eval, depth}
			}
		}
		return minimax_res{best_eval, depth}
	}
}

func EvaluateGame(game *chess.Game) float64 {
	return MaterialSum(game)
}

func MaterialSum(game *chess.Game) float64 {
	var board_value = 0.0
	var isEndGame = CheckEndGame(game)
	for square, piece := range game.Position().Board().SquareMap() {
		board_value += GetPieceValue(square, piece, isEndGame)
	}
	return board_value
}

func CheckEndGame(game *chess.Game) bool {
	var queensCount = 0
	var minorsCount = 0
	for _, piece := range game.Position().Board().SquareMap() {
		if piece.Type() == chess.Queen {
			queensCount++
		} else if piece.Type() == chess.Bishop || piece.Type() == chess.Knight {
			minorsCount++
		}
	}
	return queensCount == 0 || (queensCount <= 2 && minorsCount <= 4)
}
