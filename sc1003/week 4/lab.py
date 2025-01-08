# For beginners, all code in a single file without functions
board_size = 10
valid_orientations = ['horizontal', 'vertical']
# Exercise 1: Basic Conditional Statements
x, y = 5, 8
# TODO : 1. Check if coordinates are within the valid range
# Add you code of TODO 1 here
valid_coordinates = not ((x < 0 or x >= board_size) or (y < 0 or y >= board_size))
print(f"Coordinates ({x}, {y}) is valid: {valid_coordinates}")

#One more example
x, y = 10, -1
valid_coordinates = not ((x < 0 or x >= board_size) or (y < 0 or y >= board_size))
print(f"Coordinates ({x}, {y}) is valid: {valid_coordinates}")

# TODO : 2. Check if coordinates are within the valid range
# Copy your code of TODO 1 here to test on x, y = 10, -1
# Exercise 2: Conditional with Logical Operators
x, y, orientation = 4, 6, 'horizontal'
valid_coordinates = not ((x < 0 or x >= board_size) or (y < 0 or y >= board_size))
print(f"Input ({x}, {y}, {orientation}) is valid: {valid_coordinates}")

# TODO : 3. Validate user input for coordinates and orientation
# Add you code of TODO 3 here
#One more example
x, y, orientation = 11, 3, 'diagonal'
valid_coordinates = not ((x < 0 or x >= board_size) or (y < 0 or y >= board_size))
valid_orientation = orientation in valid_orientations
valid_input = valid_coordinates and valid_orientation
print(f"Input ({x}, {y}, {orientation}) is valid: {valid_input}")

# TODO : 4. Validate user input for coordinates and orientation
# Copy your code of TODO 3 here to test on x, y, orientation = 11, 3, 'diagonal'
# Exercise 3: Nested Conditionals
x, y, ship_length, orientation = 3, 5, 4, 'horizontal'
def is_placement_valid(x, y, ship_length, orientation):
    if not ((x < 0 or x >= board_size) or (y < 0 or y >= board_size)):
        if orientation in valid_orientations:
            x2, y2 = x + ship_length, y
            if orientation is "vertical":
                x2, y2 = x, y + ship_length
            if not ((x2 < 0 or x2 >= board_size) or (y2 < 0 or y2 >= board_size)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

placement_valid = is_placement_valid(x, y, ship_length, orientation)
print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {placement_valid}")

# TODO : 5. Validate the placement of a ship
# Add you code of TODO 5 here
#One more example
x, y, ship_length, orientation = 7, 7, 4, 'vertical'
placement_valid = is_placement_valid(x, y, ship_length, orientation)
print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {placement_valid}")

# TODO : 6. Validate the placement of a ship
# Copy your code of TODO 5 here to test on x, y, ship_length, orientation = 7, 7, 4, 'vertical'