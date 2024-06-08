def checkForGameOver(board):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    if "n" not in board:
        return True

    for fields in winning_combinations:
        if "n" != board[fields[0]] == board[fields[1]] == board[fields[2]]:
            return board[fields[0]]
    return False


def winningValue(board, player):
    boardState = checkForGameOver(board)
    if boardState == player:
        return 1
    elif boardState:
        return 0
    else:
        return -1


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
    if not max_player:
        if player == "x":
            player = "o"
        else:
            player = "x"

    if checkForGameOver(board) != False:  # noqa
        return winningValue(board, player)

    if max_player:
        value = float("-inf")
        for action in PossibleActions(board, player):
            value = max(value, MiniMax(action, player, False))
        return value

    if not max_player:
        value = float("inf")
        for action in PossibleActions(board, player):
            value = min(value, MiniMax(action, player, False))
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


yay = ['x', 'x', 'n', 'n', 'n', 'n', 'o', 'n', 'n']
#game = TicTac(players = {"x": [True, "player1"], "o": [False, "ai"]})

