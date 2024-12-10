def parse_input(data):
    # Split the input into lines
    lines = data.splitlines()
    
    # First line is the drawn numbers
    drawn_numbers = list(map(int, lines[0].split(',')))
    
    # The rest are the boards
    boards = []
    board = []
    
    for line in lines[2:]:
        if line.strip():
            # Parse each line of the board
            board.append(list(map(int, line.split())))
        else:
            # An empty line means we've finished a board
            if board:
                boards.append(board)
                board = []
    
    # Append the last board
    if board:
        boards.append(board)
    
    return drawn_numbers, boards

def mark_board(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = 'X'  # Mark the number

def has_winner(board):
    # Check for complete row or column of 'X'
    for i in range(5):
        if all(cell == 'X' for cell in board[i]):  # Row check
            return True
        if all(board[j][i] == 'X' for j in range(5)):  # Column check
            return True
    return False

def calculate_score(board, last_called_number):
    # Calculate the sum of unmarked numbers
    unmarked_sum = sum(cell for row in board for cell in row if cell != 'X')
    return unmarked_sum * last_called_number

def bingo_game(data):
    # Parse the input
    drawn_numbers, boards = parse_input(data)
    
    # List to track the state of the boards (whether they have won or not)
    won_boards = set()  # Set to keep track of indices of won boards
    last_winner_score = 0
    
    # Simulate the drawing of numbers
    for number in drawn_numbers:
        for i, board in enumerate(boards):
            if i not in won_boards:  # Only mark the board if it hasn't won yet
                mark_board(board, number)
                if has_winner(board):
                    won_boards.add(i)  # Mark this board as won
                    last_winner_score = calculate_score(board, number)
                    
    return last_winner_score  # The score of the last board to win

# # Example input
# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""

# Read input from 'input.txt'
with open('input.txt', 'r') as file:
    data = file.read()

# Solve the problem
print(bingo_game(data))
