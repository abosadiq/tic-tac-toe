# list comprehension for the game board
board = ["  " for i in range(9)]

# Function for printing the board for the Game 3 x 3


def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function for Player moves


def player_move(icon):
    choice = int(input("Enter your move (1-9): ").strip())
    if choice > 9:
        print("Invalid input Please Enter numbers (1-9) ")
    else:
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2

        print(f"Your turn player {number}")

        if board[choice - 1] == "  ":
            board[choice - 1] = icon
        else:
            print()
            print("That space is taken!")

# Function to chech the winner


def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# To check od the game is tie


def is_draw():
    if "  " not in board:
        return True
    else:
        return False


while (1):
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
