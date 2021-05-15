# ♟  MayaChess

Chess engine developped under the traditionnal minimax alpha-beta pruning algorithm, written in Go.

<p align="center">
  <img src="https://i.imgur.com/m3o3O0S.gif" alt="this slowpoke moves" />
</p>

* UCI protocol support for communication with connected chess board or chess websites API (for example : [Lichess](http://lichess.org) / [lichess-bot](https://github.com/ShailChoksi/lichess-bot)).
* Engine based on the chess library [notnil/chess](https://github.com/notnil/chess).


### Dependency tracking
```
$ go mod init github.com/arnaudperalta/mayachess
```

### Build :
```
$ go build -o mayachess src/*.go
```
