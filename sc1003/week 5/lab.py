board_size = 10
# TODO : 1. Initialize a board_sizexboard_size game board with all
# cells set to 0 (empty)
# Add you code of TODO 1 here

game_board = []
for i in range(0, 10, 1):
    row = []
    for j in range(0, 10, 1):
        row.append(0)
    game_board.append(row)
    
def is_coord_valid(x, y):
    return ((x >= 0 and x < board_size) and (y >= 0 and y < board_size))

# TODO : 2.While loop to repeatedly ask for valid attack coordinates
# Add you code of TODO 2 here
while True:
    attack_row = 0
    attack_col = 0
    while True:
        try:
            attack_row = int(input("Enter attack row (0-9): "))
            break
        except:
            print("Please enter a valid number.")
    while True:
        try:
            attack_col = int(input("Enter attack column (0-9): "))
            break
        except:
            print("Please enter a valid number.")
    is_attack_coord_valid = is_coord_valid(attack_row, attack_col)
    print(f"Coordinates ({attack_row}, {attack_col}) are valid: {is_attack_coord_valid}")
    if is_attack_coord_valid:
        game_board[attack_row][attack_col] = 1
        break
    print("Please try again.")
    

# TODO : 3. For loop to iterate through each row and column of the
# board
# Add you code of TODO 3 here
for row in game_board:
    s_row = ""
    for cell in row:
        s_row += f"{cell}"
    print(s_row)
