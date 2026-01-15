# Create an empty board with 9 spaces
board = [" " for i in range(9)]

# Function to display the board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to check if a player has won
def check_winner(player):
    # All possible winning positions
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    
    # Check each winning position
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Main game function
def play_game():
    player = "X"  # First player

    # Run the game until it ends
    while True:
        print_board()

        # Take input from player
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

        # Check if the position is valid
        if board[pos] != " ":
            print("Invalid move! Try again.")
            continue

        # Place the player's mark
        board[pos] = player

        # Check for winner
        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            break

        # Check for draw
        if " " not in board:
            print_board()
            print("Game Draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Start the game
play_game()
