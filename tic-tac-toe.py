class Player():

    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece


class Move():
    
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board():
    
    def __init__(self):
        self.moves = []
        self.current = ["   |   |   ",
                        "   |   |   ",
                        "---|---|---",
                        "   |   |   ",
                        "   |   |   ",
                        "---|---|---",
                        "   |   |   ",
                        "   |   |   "]

    def display(self):
        for row in self.current:
            print(row)

    def check_win(self):
        pass


class Game():
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def turn(self, player):
        row = int(input(f'Which row do you want to place your piece in, {player.name}? '))
        column = int(input(f'Which column do you want to place your piece in, {player.name}? '))
        row = row*3+1
        if column == 0:
            self.board.current[row] = f" {player.game_piece} |   |   "
        elif column == 1:
            self.board.current[row] = f"   | {player.game_piece} |   "
        else:
            self.board.current[row] = f"   |   | {player.game_piece} "
        self.board.display()



b = Board()
b.display()
harry = Player("Harry", "X")
hermione = Player("Hermione", "O")
g = Game(b, harry, hermione)
g.turn(harry)


