# Get the start position for the Carrier
print("Please enter start_position of Carrier in the following format (row,col). E.g. 6,4")
user_input_c = input("Enter coordinates: ")
x_c, y_c = user_input_c.split(",")
x_c, y_c = int(x_c), int(y_c)

# TODO : 1. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 1 here
# Get the start position for the Submarine
print("Please enter start_position of Submarine in the following format (row,col). E.g. 6,4")
user_input_s = input("Enter coordinates: ")
x_s, y_s = user_input_s.split(",")
x_s, y_s = int(x_s), int(y_s)

# TODO : 2. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 2 here

# TODO : 3. Dictionary to store ship details (name, length, and starting coordinates)
# Add you code of TODO 3 here
ships = {
    "Carrier": {
        "id": "S",
        "length": 5,
        "start_pos": (x_c, y_c)
    },
    "Submarine": {
        "id": "S",
        "length": 3,
        "start_pos": (x_s, y_s)
    }
}

#code from lab4
# Initialize a board_size x board_size game board with all cells set to 0 (empty)
board_size = 10
game_board = []
for i in range(0, board_size, 1):
    row = []
    for j in range(0, board_size, 1):
        row.append(0)
    game_board.append(row)

def place_ship(ship_name):
    ship = ships.get(ship_name)
    if ship is None:
        raise Exception(f"{ship_name} does not exist.")
    id = ship["id"]
    length = ship["length"]    
    x, y = ship["start_pos"]    
    for i in range(0, length):
        game_board[x][y + i] = id
        
# TODO : 4.Function to place ships on the board based on their start position and length
# Add you code of TODO 4 here

# Place the ships on the board
place_ship("Carrier")
place_ship("Submarine")
#code from lab4
# While loop to repeatedly ask for valid attack coordinates
def is_coord_valid(x, y):
    return ((x >= 0 and x < board_size) and (y >= 0 and y < board_size))
while True:
    attack_row = int(input("Enter attack row (0-9): "))
    attack_col = int(input("Enter attack column (0-9): "))
    is_attack_coord_valid = is_coord_valid(attack_row, attack_col)
    print(f"Coordinates ({attack_row}, {attack_col}) are valid: {is_attack_coord_valid}")
    if is_attack_coord_valid:
        game_board[attack_row][attack_col] = 1
        break

#code from lab4
# For loop to iterate through each row and column of the board
for row in game_board:
    s_row = ""
    for cell in row:
        s_row += f"{cell}"
    print(s_row)
