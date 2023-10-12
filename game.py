from player import Player
from board import Board


class Game:
    def __init__(self) -> None:
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()
        self.current = self.player1

    def run(self):
        while not self.is_over:
            print(self.board)
            print(f"It's {self.current.value}'s turn")
            while True:
                try:
                    pos = self.current.get_pos()
                    self.board[pos] = self.current.value
                    break
                except ValueError as e:
                    print(e)
            self.swap_player()

        if self.board.is_have_winner:
            self.swap_player()
            print(f"Winner is {self.current.value}")

    @property
    def is_over(self):
        return self.board.is_full or self.board.is_have_winner

    def swap_player(self):
        self.current = self.player1 if self.current is self.player2 else self.player2
