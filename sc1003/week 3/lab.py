# Pseudocode initializing the board
# Initialize width to 10
# Initialize height to 10
# Initialize layer to 2
# Initialize the board as a 3D string list of size, depth, width, height

# Pseudocode for placing ships
# # Choosing orientation
# Initialize orientation to None
# While True
#  Input the orientation of the ship
#  If orientation is not ("h" or "v") Then
#   Continue
#  EndIf
#  Break
# EndWhile
# 
# # Choosing coordinates
# While True
#  Input the coordinates to place the ship
#  Initialize split_coordinates to coordinates.split() by ","
#  If split_coordinates length is not 3 Then
#   Continue
#  EndIf
#  Initialize row to split_coordinates[0]
#  Initialize _column to split_coordinates[1]
#  Initialize _depth to split_coordinates[2]
#  If row is not [A...J] Then
#   Continue
#  EndIf
#  If _column is not an integer Then
#   Continue
#  EndIf
#  If _depth is not an integer Then
#   Continue
#  EndIf
#  Initialize column, depth to int(_column), int(_depth)
# EndWhile

# Initialize the playe_1 name as string
# Initialize the player_2 name as string



# TODO : 1. There are two players in the game. Initialize their names as string
# Input the names of player 1
# Add you code of TODO 1 here

player1 = "Player 1"
player2 = "Player 2"

# TODO : 2. There are two layers in the sea. Initialize the integer variable layer
# Add you code of TODO 2 here

layer = 2

# TODO : 3. The battleship board is 10 by 10 dimension. Initialize the integer variables
# width and height
# Add you code of TODO 3 here

width = 10
height = 10

underwater_board = [[" " for _ in range(width)] for _ in range(height)]
surface_board = [[" " for _ in range(width)] for _ in range(height)]
board = [underwater_board, surface_board]

def print_board(depth = 0):
    print(f"---------- Layer {depth} ----------")
    layer = ""
    for row in range(height):
        str_row = ""
        for column in range(width):
            str_row += board[depth][row][column]
        layer += str_row + "\n"
    print(layer)

# board[0][3][4] = "X"
# print_board()

# TODO : 4. Initialize a boolean variable that will be used to indicate
# whether user input is valid or not, two boolean variables hit and miss that indicate
# whether the ship is hit or missed
# Add you code of TODO 4 here

is_valid = False
hit = False
miss = False

# Placement of ships
ship_types = ["C", "S"]
ships_left = ["C", "S"]
while True:
    # TODO : 5. The ships have only two orientation, either vertical or horizontal.
    # Initialize a variable as ship orientation
    # Add you code of TODO 5 here
    
    orientation = input("Enter orientation (h or v): ")
    if orientation not in ["h", "v"]:
        continue

    # TODO : 6. The coordinates of where to put ship or where to hit on the board have a
    # specific format. Create a string variable as coordinates
    # Add you code of TODO 6 here
    while True:
        coords = input("Enter coordinates: ")
        split_coords = coords.split(",")
        if len(split_coords) != 3:
            print("Invalid coordinates, must be in the format (row [a-j], column [0-9], depth [0-1])")
            continue
        row = split_coords[0].lower()
        column = split_coords[1]
        depth = split_coords[2]
        if row not in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]:
            print("Invalid row, must be in the format (row [a-j])")
            continue
        try:
            column = int(column)
            depth = int(depth)
        except ValueError:
            print("Invalid column and depth must be an integer")
            continue
        if column < 0 or column > 9 or depth < 0 or depth > 1:
            print("Invalid column and depth must be in the range [0-9] and [0-1]")
            continue
        
        ship = input("Enter ship type (C or S): ")
        if ship not in ship_types:
            print("Invalid ship type, must be in the format (C or S)")
            continue
        break   
        
    break


# TODO : 7. There are only two types of ships. Initialize two string variables as ship names
# Add you code of TODO 7 here
# TODO : 8. Initialize a string variable holding a welcome message that can be displayed to user
# Add you code of TODO 8 here

# print(player1, player2)
# print(layer)
# print(width, height)
# print(valid, hit, miss)
# print(ori)
# print(coor)
# print(ship1, ship2)
# print(welmes)

# TODO : 9. Take user input for attack coordinates and display the result.
# Add you code of TODO 9 here
