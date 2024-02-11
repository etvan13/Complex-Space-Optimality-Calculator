import math

# Function to calculate the shortest distance from the current position to the target point
### HYPOTENUSE ###
def calculate_shortest_distance(current_x, current_y, target_x, target_y):
    return math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)

# Function to move towards or away from the target point, adjusted for direct jump to target
### Changes X and Y for hypotenuse traversal ###
def move_towards_away(current_x, current_y, target_x, target_y, move_away=False):
    # Calculate the direction vector components from the current position to the target
    direction_x = target_x - current_x
    direction_y = target_y - current_y
    
    # Calculate the magnitude of the direction vector
    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
    
    # Normalize the direction vector to get a unit vector
    if magnitude > 0:
        unit_direction_x = direction_x / magnitude
        unit_direction_y = direction_y / magnitude
    else:
        # If the current position is already at the target, no movement is needed
        return current_x, current_y
    
    # Determine the new position based on whether moving towards or away from the target
    if move_away:
        # Move 1 unit away from the target by subtracting the unit vector components from the current position
        new_x = current_x - unit_direction_x
        new_y = current_y - unit_direction_y
    else:
        # Move 1 unit towards the target by adding the unit vector components to the current position
        new_x = current_x + unit_direction_x
        new_y = current_y + unit_direction_y
    
    return new_x, new_y



# Function to simulate traversal towards the target point
def simulate_traversal(start_x, start_y, target_x, target_y):
    current_x, current_y = start_x, start_y
    real_traversal = 0  # Real traversal's initial position
    shortest_distance = calculate_shortest_distance(start_x, start_y, target_x, target_y)
    initial_shortest_distance = shortest_distance #For rate calculation

    print(f"Starting at: ({start_x}, {start_y})")
    print(f"Getting to point: ({target_x}, {target_y})")
    print(f"Current shortest distance: {shortest_distance}")   
    print()

    while True:
        # Check if the last step is < 1 unit away for complex traversal

        move = input("Enter movement direction (l/r/u/d/t/a/e): ")
        
        if shortest_distance < 1:
            current_x, current_y = target_x, target_y  # Move directly to the target
            print("Complex traversal: Making the final step directly to the target.")

        else:
            if move in 'lrudta':
                if move == 'l':  # Left
                    current_x -= 1
                elif move == 'r':  # Right
                    current_x += 1
                elif move == 'u':  # Up
                    current_y += 1
                elif move == 'd':  # Down
                    current_y -= 1
                elif move == 't':  # Towards the target
                    new_x, new_y = move_towards_away(current_x, current_y, target_x, target_y, move_away=False)
                    current_x, current_y = new_x, new_y
                elif move == 'a':  # Away from the target
                    new_x, new_y = move_towards_away(current_x, current_y, target_x, target_y, move_away=True)
                    current_x, current_y = new_x, new_y

            elif move == 'e':  # Exit
                break

        # Calculate the shortest distance in the complex plane
        shortest_distance = calculate_shortest_distance(current_x, current_y, target_x, target_y)

        # Using ceiling of shortest distance to ensure we're dealing with whole steps
        steps_to_target = math.ceil(shortest_distance)

        remaining_real_distance = initial_shortest_distance - real_traversal

        real_distance_rate = remaining_real_distance / (steps_to_target + 1)

        # Update real traversal with the recalculated rate
        real_traversal += real_distance_rate 

        print(f"Complex Current Position: ({current_x}, {current_y})")
        print(f"Distance to B (Shortest distance): {shortest_distance}({math.ceil(shortest_distance)} steps)")
        print(f"Current Rate: {real_distance_rate}")
        print(f"Real Traversal: {real_traversal}")
        print()

        # Check if the complex position has reached the target
        if ((current_x == target_x) and (current_y == target_y)):
            print("You've reached the target point!")
            break

# Example usage:
start_x, start_y = 0, 0
target_x, target_y = 3, 4

simulate_traversal(start_x, start_y, target_x, target_y)


#Fix a few things.
#When the final step is <1, it hops over it
#Figure out ceil better, like what it is for (obv for making hypotenuse whole numbers)
    #These aren't numbers, they're steps of progression, one step is anything between 0 and 1
    # but it typically just increments by 1 unless the last step is <1, then it increments to the spot