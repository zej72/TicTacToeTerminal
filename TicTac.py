import random


def isTerminalState(board) -> bool or str:
    terminal_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for ter_pos in terminal_positions:
        if board[ter_pos[0]] == board[ter_pos[1]] == board[ter_pos[2]] != "n":
            return board[ter_pos[0]]  # someone won

    if "n" not in board:
        return True  # draw

    return False  # not terminal


def winningValue(board, player) -> int:
    game_state = isTerminalState(board)
    if game_state == player:
        return 1
    elif game_state == switch(player):
        return -1
    else:
        return 0


def PossibleActions(board, player) -> list:
    i = 0
    possible_actions = []
    while i <= len(board):
        if board[i] == "n":
            action = []
            # copy list bc normal way is broken god help me
            for item in board:
                action.append(item)

            action[i] = player
            possible_actions.append(action)
        i += 1
    return possible_actions


def MiniMax(board, is_maximizing) -> int:
    if isTerminalState(board):
        return winningValue(board, "max")

    if is_maximizing:
        best_score = float("-inf")
        i = 0
        while i <= 8:
            if board[i] == "n":
                board[i] = "max"
                score = MiniMax(board, False)
                board[i] = "n"
                if score > best_score:
                    best_score = score
            i += 1
        return best_score
    else:
        best_score = float("inf")
        i = 0
        while i <= 8:
            if board[i] == "n":
                board[i] = "min"
                score = MiniMax(board, True)
                board[i] = "n"
                if score < best_score:
                    best_score = score
            i += 1
        return best_score


def GetOptimalMove(board, player) -> int:
    best_score = float("-inf")
    move = str

    f_board = []
    for field in board:
        f_board.append(field)

    if board == ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']:
        return random.choice([1, 3, 7, 9])

    i = 0
    while i <= 8:
        if f_board[i] == player:
            f_board[i] = "max"
        elif f_board[i] != "n":
            f_board[i] = "min"
        i += 1

    i = 0
    while i <= 8:
        if f_board[i] == "n":
            f_board[i] = "max"
            score = MiniMax(f_board, False)
            f_board[i] = "n"
            if score > best_score:  # or (random.randrange(2) == 1 and score == best_score):
                best_score = score
                move = i
        i += 1

    if best_score == 1:
        print("gg")

    return move + 1


def switch(inp) -> str:
    if inp == "o":
        return "x"
    elif inp == "x":
        return "o"
    elif inp == "max":
        return "min"
    elif inp == "min":
        return "max"
    else:
        raise TypeError(f"value: {inp} not supported")


class TicTac:

    def __init__(self, players):
        self.players = players
        self.board = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
        self.active_player = "x"

    def printBoard(self) -> None:
        horizontal_field = 0
        vertical_field = 0
        out = ""

        for field in self.board:
            out += " "
            horizontal_field += 1
            if field == "n":
                out += " "
                #out += str(horizontal_field + vertical_field * 3)
            if field == "x":
                out += "x"
            if field == "o":
                out += "o"

            if horizontal_field >= 3 and vertical_field < 2:
                out += "\n────╂─────╂────\n"
                horizontal_field = 0
                vertical_field += 1
            elif horizontal_field != 3:
                out += "  ┃ "
        print(out + "\n\n")

    def move(self, move_id) -> None:
        move_id -= 1
        if self.board[move_id] == "n":
            self.board[move_id] = self.active_player

            if self.active_player == "x":
                self.active_player = "o"
            else:
                self.active_player = "x"
        else:
            print(f"field {move_id} is occupied by {self.board[move_id]}\n{self.board}")
            raise Exception("field is occupied")


if __name__ == "__main__":
    test_board = ['x', 'n', 'n', 'n', 'n', 'n', 'o', 'n', 'x']
    print(GetOptimalMove(test_board, "o"))
