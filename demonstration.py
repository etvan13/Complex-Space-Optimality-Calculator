import math

# Function to calculate the distance to B
def calculate_distance(x, bx):
    return abs(bx - x)

def main():
    ax = 0  # Point A on x-axis
    bx = 10  # Point B on x-axis

    real_distance = 0
    real_distance_rate = 1

    i_real_distance = 0  # Total distance considering imaginary

    print(f"Starting at: ({ax}, {0})")
    print(f"Getting to point: ({bx}, {0})")
    print(f"Current shortest distance: {bx-ax}")   
    print()

    while True:
        move = input("Enter movement direction (l/r/e): ")

        # Update position based on input
        if move == 'l':
            ax -= 1
        elif move == 'r':
            ax += 1
        elif move == 'e':  # Exit condition
            break
        else:
            continue  # If the input is not recognized, continue to the next iteration of the loop

        curr_distance = calculate_distance(ax, bx)

        # In the event of moving 'away' from point or 'decelerating'
        # '+1' accounts for the first step rate to avoid division by zero
        real_distance_rate = (bx - real_distance) / (curr_distance + 1)

        # Adds the rate to the distance for one unit of movement
        real_distance += real_distance_rate

        i_real_distance += 1  # Increment total distance considering imaginary

        print(f"Current Position: ({ax}, 0)")
        print(f"Distance to B: {curr_distance}")
        print(f"Current Rate: {real_distance_rate}")
        print(f"Real Traversal: {real_distance}")
        print(f"Real + Imaginary Distance: {i_real_distance}")
        print()

        if ax == bx:
            print("You've reached the designated point!")
            break

if __name__ == "__main__":
    main()
