package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/notnil/chess"
)

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var cmd string
	game := chess.NewGame()

	for {
		cmd, _ = reader.ReadString('\n')
		cmd = strings.TrimSuffix(cmd, "\n")
		uci_command(&game, cmd)
	}
}

func uci_command(game **chess.Game, cmd string) {
	if cmd == "quit" {
		os.Exit(1)
	}

	if cmd == "uci" {
		fmt.Println("id name Maya Chess")
		fmt.Println("id author Arnaud Peralta")
		fmt.Println("uciok")
	}

	if strings.Contains(cmd, "isready") {
		fmt.Println("readyok")
	}

	if strings.Contains(cmd, "position startpos moves") {
		var moves = strings.Split(cmd, " ")[3:]
		*game = chess.NewGame(chess.UseNotation(chess.UCINotation{}))
		for _, v := range moves {
			(*game).MoveStr(v)
		}
	}

	if strings.Contains(cmd, "position fen") {
		var fen_str = strings.Join(strings.Split(cmd, " ")[2:], " ")
		fen, err := chess.FEN(fen_str)
		if err != nil {
			return
		}
		*game = chess.NewGame(fen)
		fmt.Println((*game).FEN())
	}

	if strings.Contains(cmd, "go") {
		var move = Find_best_move(*game, 3)
		(*game).Move(move)
		fmt.Printf("bestmove %s\n", move)
	}
	//fmt.Println((*game).Position().Board().Draw())
}
