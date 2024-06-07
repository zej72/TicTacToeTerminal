class TicTac:

    def __init__(self, players):
        self.players = [False, False]
        self.positions = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']

    def getAvailableMoves(self):
        return self.positions.count('n')

    def getPositions(self):
        return self.positions

    def printPositions(self):
        position_selector = 1
        horizontal_field = 0
        vertical_field = 0
        out = ""

        for field in self.positions:
            out += " "
            horizontal_field += 1
            if field == "n":
                out += str(position_selector)
                position_selector += 1
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

    def move(self, player, move_id):
        self.positions[move_id] = player
