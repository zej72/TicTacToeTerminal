from brain import TicTac

#  1  ┃  2  ┃  3
# ────╂─────╂────
#  4  ┃  5  ┃  6
# ────╂─────╂────
#  7  ┃  8  ┃  9

while True:
    player = input("1th player: o or x?\n")
    if player == "o" or player == "x":
        break

while True:
    coplayer = input("2th player: AI? (y/n)\n")
    if coplayer == "y" or coplayer == "n":
        break

if coplayer == "y":
    players = {"x": True, "o": True}
elif player == "x":
    players = {"x": True, "o": False}
else:
    players = {"x": False, "o": True}

game = TicTac(players)

while True:
    game.printPositions()
    move = int(input())

    if 0 < move <= game.getAvailableMoves():
        game.move("x")
