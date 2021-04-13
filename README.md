# ♟  MayaChess

Chess engine developped under the traditionnal minimax alpha-beta pruning algorithm.

<p align="center">
  <img src="https://i.imgur.com/m3o3O0S.gif" alt="this slowpoke moves" />
</p>

## Features
* UCI protocol support for communication with connected chess board or chess websites API (for example : [Lichess](http://lichess.org) / [lichess-bot](https://github.com/ShailChoksi/lichess-bot)).
* Engine based on the library python-chess for an easy maintainability.
* Jupyter notebook demo file (`src/mayachess.ipynb`)


## Installation
```
$ pip3 install -r requirements.txt
```

## Deployment into a standalone executable file with PyInstaller :
```
$ cd src/
$ pyinstaller --onefile main.py
```
