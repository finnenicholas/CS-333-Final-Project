def main():
  player = 0
  winner = False
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  stalemate = False
  while not winner and not stalemate:
    valid_move = False
    move = None
    display_board(board)
    while not valid_move:
      move = input(f"{player + 1}: Enter your move: ")
      valid_move = validate_move(player, board, move)
    board = place_mark(player, board, move)
    stalement = check_for_stalemate(board)

    if stalement:
      print("Stalemate!")

    winner = check_for_win(board)
    player = 1 if player == 0 else 0
    print("\n")

  print(f"Player {player} wins!")


def display_board(board) -> None:
  for line in board:
    print(line)


def place_mark(player, board, position):
  x, y = position
  if player == 0:
    board[int(x)][int(y)] = "O"
  else:
    board[int(x)][int(y)] = "X"
  return board


def validate_move(player, board, move) -> bool:
  if move[0] not in ["0", "1", "2"] and move[1] not in ["0", "1", "2"]:
    return False
  else:
    return True


def check_for_win(board) -> bool:

  #Checking Accross
  for i, e in enumerate(board):
    if (board[i][0] == board[i][1] == board[i][2] != " "):
      return True

  #Checking Down
  for i, e in enumerate(board):
    if (board[0][i] == board[1][i] == board[2][i] != " "):
      return True

  #Checking Diagonal
  if (board[0][0] == board[1][1] == board[2][2] != " "):
    return True

  if (board[0][2] == board[1][1] == board[2][0] != " "):
    return True

  return False


def check_for_stalemate(board) -> bool:
  for i, e in enumerate(board):
    for j, e in enumerate(board):
      if board[i][j] == " ":
        return False
  return True


if __name__ == '__main__':
  main()

