def checkForGameOver(board):
    winning_combinations = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

    i = -1
    while i < len(winning_combinations) - 1:
        i += 1
        if "n" != board[winning_combinations[i][0]] == board[winning_combinations[i][1]] == board[winning_combinations[i][2]]:
            return board[winning_combinations[i][0]]

    if "n" in board:
        return False
    return True


def winningValue(board, player):
    boardState = checkForGameOver(board)
    if boardState == player:
        return 1
    elif boardState == True:  # noqa
        return 0
    elif boardState != player:
        return -1


def switch(inp):
    if inp == "o":
        return "x"
    elif inp == "x":
        return "o"
    else:
        raise TypeError("can accept only 'o' and 'x'")


def PossibleActions(board, player):
    possible_actions = []
    i = 0
    while i < len(board):
        if board[i] == "n":
            possible_action = []
            for item in board:
                possible_action.append(item)
            possible_action[i] = player
            possible_actions.append(possible_action)
            board[i] = "n"
        i += 1
    return possible_actions


def MiniMax(board, player, max_player):

    game_over_check = checkForGameOver(board)
    if game_over_check == True or game_over_check == "x" or game_over_check == "o":  # noqa
        return winningValue(board, player)

    if max_player:
        value = -9999999
        for position in PossibleActions(board, switch(player)):
            value = max(value, MiniMax(position, player, False))
        return value

    if not max_player:
        value = 9999999
        for position in PossibleActions(board, player):
            value = min(value, MiniMax(position, player, True))
        return value


class TicTac:

    def __init__(self, players):
        self.players = players
        self.board = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
        self.active_player = "x"

    def getAvailableMoves(self):
        return self.board.count('n')

    def printBoard(self):
        horizontal_field = 0
        vertical_field = 0
        out = ""

        for field in self.board:
            out += " "
            horizontal_field += 1
            if field == "n":
                out += str(horizontal_field + vertical_field * 3)
            if field == "x":
                out += "✕"
            if field == "o":
                out += "◯"

            if horizontal_field >= 3 and vertical_field < 2:
                out += "\n────╂─────╂────\n"
                horizontal_field = 0
                vertical_field += 1
            elif horizontal_field != 3:
                out += "  ┃ "
        print(out)

    def move(self, move_id):
        move_id -= 1
        if self.board[move_id] == "n":
            self.board[move_id] = self.active_player

            if self.active_player == "x":
                self.active_player = "o"
            else:
                self.active_player = "x"
        else:
            raise Exception("field is occupied")

#yay = ['x', 'x', 'n', 'n', 'n', 'n', 'o', 'n', 'n']
#game = TicTac(players = {"x": [True, "player1"], "o": [False, "ai"]})
