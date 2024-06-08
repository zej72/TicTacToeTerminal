def checkForWin(board):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for fields in winning_combinations:
        if "n" != board[fields[0]] == board[fields[1]] == board[fields[2]]:
            winner = board.board[fields[0]]
            return winner
    return False


def minimax():
    pass


class TicTac:

    def __init__(self, players):
        self.players = players
        self.board = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
        self.active_player = "x"
        self.AiMode = "normal"

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
