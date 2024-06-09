from TicTac import *
from time import sleep

#  1  ┃  2  ┃  3
# ────╂─────╂────
#  4  ┃  5  ┃  6
# ────╂─────╂────
#  7  ┃  8  ┃  9

players = {"x": [True, ""], "o": [True, ""]}

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
AI_coplayer_enable = True
while AI_coplayer_enable:
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
while True:
    game = TicTac(players)

    game_active = True

    while game_active:
        game.printBoard()
        if isTerminalState(game.board):
            winner = isTerminalState(game.board)
            if winner:
                print("draw!")
            else:
                print(f"{winner} won!")
            game_active = False
            continue
        print(game.active_player)

        if game.players[game.active_player][0]:
            move = int(input(game.active_player))
            try:
                game.move(move)
            except Exception as e:
                print(e)
        else:
            move = GetOptimalMove(game.board, game.active_player)
            print(move)
            game.move(move)

    game.board = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
    sleep(1)
    print("\n\n\n\n\n\n\nroles switched\nprevious x is now o and previous o is now x!")
    game.players["x"][0] = not game.players["x"][0]
    game.players["o"][0] = not game.players["o"][0]
