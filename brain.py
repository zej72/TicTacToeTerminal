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
