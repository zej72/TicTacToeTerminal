class TicTac:

    def __init__(self, players):
        self.players = players
        self.positions = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
        self.active_player = "x"

    def getAvailableMoves(self):
        return self.positions.count('n')

    def getPositions(self):
        return self.positions

    def printBoard(self):
        horizontal_field = 0
        vertical_field = 0
        out = ""

        for field in self.positions:
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
        if self.positions[move_id] == "n":
            self.positions[move_id] = self.active_player

            if self.active_player == "x":
                self.active_player = "o"
            else:
                self.active_player = "x"
        else:
            raise Exception("field is occupied")

    def checkForWin(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for fields in winning_combinations:
            if "n" != self.positions[fields[0]] == self.positions[fields[1]] == self.positions[fields[2]]:
                winner = self.positions[fields[0]]
                winner_name = self.players[winner][1]

                print(f"{winner_name} ({winner}) WON!")
                exit(1)
