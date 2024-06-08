from TicTac import *

#  1  ┃  2  ┃  3
# ────╂─────╂────
#  4  ┃  5  ┃  6
# ────╂─────╂────
#  7  ┃  8  ┃  9

players = {"x": [False, ""], "o": [False, ""]}

# get player 1 character

while True:
    player = input("1th player: o or x?\n")
    if player == "o":
        players["o"] = [True, "player1"]
        break
    elif player == "x":
        players["x"] = [True, "player1"]
        break

# get player 2/ AI character

while True:
    coplayer = input("2th player: AI? (y/n)\n")
    if coplayer == "y":
        if player == "o":
            players["x"] = [False, "AI"]
        elif player == "x":
            players["o"] = [False, "AI"]
        break
    elif coplayer == "n":
        if player == "o":
            players["x"] = [True, "player2"]
        elif player == "x":
            players["o"] = [True, "player2"]
        break

game = TicTac(players)

while True:
    game.printBoard()
    if checkForGameOver(game.board):
        winner = winningValue(game.board, "x")
        if winner == 1:
            print("✕ won!")
        elif winner == 0:
            print("draw!")
        elif winner == -1:
            print("◯ won!")
        exit(1)

    print(game.active_player)

    if game.players[game.active_player][0]:
        move = int(input(game.active_player))
        try:
            game.move(move)
        except Exception as e:
            print(e)
    else:
        moves = []
        for item in PossibleActions(game.board, "x"):
            move = [MiniMax(item, "x", True), item]
            moves.append(move)
            print(move)
        i = 1
        while i >= -1:
            for item in moves:
                if item[0] == i:
                    move = item[1]
                    i = -2
                    print(f"found best move: {move} winning probability: {item[0]}")
                    break
            i -= 1

        game.board = move

        if game.active_player == "x":
            game.active_player = "o"
        else:
            game.active_player = "x"
