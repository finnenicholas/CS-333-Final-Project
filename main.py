class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0
        self.winner = None
        self.stalemate = False

    def display_board(self):
        print("\n")
        print(" | ".join(self.board[0]))
        print("-" * 5)
        print(" | ".join(self.board[1]))
        print("-" * 5)
        print(" | ".join(self.board[2]))
        print("\n")

    def place_mark(self, x, y):
        if self.board[x][y] == " ":
            self.board[x][y] = "O" if self.current_player == 0 else "X"
            return True
        return False

    def validate_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == " "

    def check_for_win(self):
        lines = self.board + [list(t) for t in zip(*self.board)]
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])
        for line in lines:
            if line.count(line[0]) == 3 and line[0] != " ":
                return True
        return False

    def check_for_stalemate(self):
        if any(" " in row for row in self.board):
            return False
        self.stalemate = True
        return True

    def next_turn(self):
        self.current_player = 1 - self.current_player

    def play(self):
        while not self.winner and not self.stalemate:
            self.display_board()
            move_valid = False
            while not move_valid:
                move = input(f"Player {self.current_player + 1} ({'O' if self.current_player == 0 else 'X'}), enter your move (row col): ").split()
                if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                    x, y = int(move[0]), int(move[1])
                    move_valid = self.validate_move(x, y) and self.place_mark(x, y)

            if self.check_for_win():
                self.winner = self.current_player
                print(f"Player {self.current_player + 1} ({'O' if self.current_player == 0 else 'X'}) wins!")
                self.display_board()
            elif self.check_for_stalemate():
                print("Stalemate!")
                self.display_board()
            else:
                self.next_turn()


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
