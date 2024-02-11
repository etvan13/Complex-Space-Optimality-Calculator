import math

# Function to calculate the shortest distance in 3D space
def calculate_shortest_distance(current_x, current_y, current_z, target_x, target_y, target_z):
    return math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2 + (target_z - current_z) ** 2)

# Function to move towards or away from the target point in 3D space
def move_towards_away_3d(current_x, current_y, current_z, target_x, target_y, target_z, move_away=False):
    # Calculate the direction vector components from the current position to the target
    direction_x = target_x - current_x
    direction_y = target_y - current_y
    direction_z = target_z - current_z
    
    # Calculate the magnitude of the direction vector in 3D
    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2 + direction_z ** 2)
    
    # Normalize the direction vector to get a unit vector
    if magnitude > 0:
        unit_direction_x = direction_x / magnitude
        unit_direction_y = direction_y / magnitude
        unit_direction_z = direction_z / magnitude
    else:
        # If the current position is already at the target, no movement is needed
        return current_x, current_y, current_z
    
    # Determine the new position based on whether moving towards or away from the target
    if move_away:
        # Move 1 unit away from the target by subtracting the unit vector components
        new_x = current_x - unit_direction_x
        new_y = current_y - unit_direction_y
        new_z = current_z - unit_direction_z
    else:
        # Move 1 unit towards the target by adding the unit vector components
        new_x = current_x + unit_direction_x
        new_y = current_y + unit_direction_y
        new_z = current_z + unit_direction_z
    
    return new_x, new_y, new_z

# Function to simulate traversal towards the target point in 3D space
def simulate_traversal_3d(start_x, start_y, start_z, target_x, target_y, target_z):
    current_x, current_y, current_z = start_x, start_y, start_z
    real_traversal = 0  # Real traversal's initial position
    initial_shortest_distance = calculate_shortest_distance(start_x, start_y, start_z, target_x, target_y, target_z)

    print(f"Starting at: ({start_x}, {start_y}, {start_z})")
    print(f"Getting to point: ({target_x}, {target_y}, {target_z})")
    print(f"Current shortest distance: {initial_shortest_distance}")   
    print()

    while True:
        # Calculate the shortest distance in 3D space
        shortest_distance = calculate_shortest_distance(current_x, current_y, current_z, target_x, target_y, target_z)

        move = input("Enter movement direction (l/r/u/d/f/b/t/a/e): ")

        # Check if the last step is < 1 unit away for complex traversal
        if shortest_distance < 1:
            current_x, current_y, current_z = target_x, target_y, target_z  # Move directly to the target
            print("Complex traversal: Making the final step directly to the target.")

        else:
            if move in 'lrudfbta':
                if move == 'l':  # Left
                    current_x -= 1
                elif move == 'r':  # Right
                    current_x += 1
                elif move == 'u':  # Up
                    current_y += 1
                elif move == 'd':  # Down
                    current_y -= 1
                elif move == 'f':  # Forwards
                    current_z += 1
                elif move == 'b':  # Backwards
                    current_z -= 1
                elif move == 't':  # Towards the target
                    current_x, current_y, current_z = move_towards_away_3d(current_x, current_y, current_z, target_x, target_y, target_z, move_away=False)
                elif move == 'a':  # Away from the target
                    current_x, current_y, current_z = move_towards_away_3d(current_x, current_y, current_z, target_x, target_y, target_z, move_away=True)

            elif move == 'e':  # Exit
                break

        # Update real traversal
        steps_to_target = math.ceil(shortest_distance)
        remaining_real_distance = initial_shortest_distance - real_traversal
        real_distance_rate = remaining_real_distance / max(1, steps_to_target)

        # Update real traversal with the recalculated rate
        real_traversal += real_distance_rate

        print(f"Complex Current Position: ({current_x}, {current_y}, {current_z})")
        print(f"Distance to B (Shortest distance): {shortest_distance} ({math.ceil(shortest_distance)} steps)")
        print(f"Current Rate: {real_distance_rate}")
        print(f"Real Traversal: {real_traversal}")
        print()

        # Check if both complex and real traversals have reached the target
        if current_x == target_x and current_y == target_y and current_z == target_z and real_traversal >= initial_shortest_distance:
            print("Both complex and real traversals have reached the target point!")
            break

# Example usage:
start_x, start_y, start_z = 0, 0, 0
target_x, target_y, target_z = 3, 4, 5

simulate_traversal_3d(start_x, start_y, start_z, target_x, target_y, target_z)
