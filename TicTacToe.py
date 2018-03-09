class Board():
    def __init__(self):
        self.boxes = [" "]*9
        self.player = "X"

    @property
    def rows(self):
        return [self.boxes[0:3], self.boxes[3:6], self.boxes[6:9]]

    @property
    def columns(self):
        return [self.boxes[0:7:3], self.boxes[1:8:3], self.boxes[2:9:3]]

    @property
    def diagonals(self):
        return [self.boxes[0:9:4], self.boxes[2:7:2]]

    @property
    def winner(self):
        for line in self.rows + self.columns + self.diagonals:
            if set(line) == {"X"}: return "X"
            elif set(line) == {"O"}: return "O"
        return None

    def print_board(self):
        print("\n\n\n" + ("\n--+---+--\n").join(" | ".join(box for box in row) for row in self.rows) + "\n\n\n")

    def play(self, box):
        if box < 1 or box > 9: raise IndexError
        if self.boxes[box-1] != " ": raise AssertionError
        self.boxes[box-1] = self.player
        self.player = "X" if self.player == "O" else "O"


print("Let's play TicTacToe!")
print("To make a move, enter the corresponding box number as shown in the diagram below:")
print("""\n\n
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
\n\n""")
print("Okay, let's start.")
game = Board()

while (not game.winner):
    game.print_board()
    print("Player {}, it's your turn!".format(game.player))
    move = input("Choose a box to play in: ")
    try:
        game.play(int(move))
    except (ValueError, IndexError):
        print("Please enter a valid box number between 1 and 9.")
    except AssertionError:
        print("That box is already taken! You can't play there.")

print("Congratulations player {}, you won!".format("X" if game.player == "O" else "O"))
game.print_board()