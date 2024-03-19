import math
from decimal import Decimal, getcontext

# Set the desired precision to 50 significant digits
getcontext().prec = 50
getcontext().Emin = -999999 #Set low to avoid scientific notation

# Function to calculate the distance to B
def calculate_distance(x, final_pt):
    return abs(final_pt - x)

def main():
    curr_pt = Decimal('0') # Point A on x-curr_ptis
    final_pt = Decimal(input("Enter the point to reach (Non-zero Positive Integer): "))  # Point B on x-curr_ptis

    real_distance = Decimal('0')
    real_distance_rate = Decimal('1')
    flip_real_distance = Decimal('0')

    i_real_distance = Decimal('0')  # Total distance considering imaginary

    print("Note, each 'left' and 'right' YOU input is considered 1 unit per 1 second of traversal for yourself")
    print(f"Starting at: ({curr_pt}, {0})")
    print(f"Getting to point: ({final_pt}, {0})")
    print(f"Current shortest distance: {final_pt - curr_pt}")   

    while True:
        print()
        move = input("Enter movement direction (l(add gravity)/r(natural flow forwards): ")
        print()
        print("----------------------------------------------------------")

        # Update position based on input
        if move == 'l':
            curr_pt -= Decimal('1')
        elif move == 'r':
            curr_pt += Decimal('1')
        elif move == 'e':  # Exit condition
            break
        else:
            continue  # If the input is not recognized, continue to the next iteration of the loop

        curr_distance = calculate_distance(curr_pt, final_pt)

        # In the event of moving 'away' from point or 'decelerating'
        # '+1' accounts for the first step rate to avoid division by zero
        real_distance_rate = (final_pt - real_distance) / (curr_distance + Decimal('1'))
        #Flip perspective calculations
        flip_real_distance_rate = Decimal('1') / real_distance_rate

        # Adds the rate to the distance for one unit of movement
        real_distance += real_distance_rate
        #Flip real distance
        flip_real_distance += flip_real_distance_rate

        #final point for flipped perspective
        flip_final_pt = flip_real_distance + ((flip_real_distance_rate**Decimal('2')) * (final_pt - real_distance))

        i_real_distance += Decimal('1')  # Increment total distance considering imaginary
        
        # Two perspectives equal in value initially.

        # Add gravity to one, and the initial perspective views 
        # the new perspective as slower. The new perspective 
        # views the initial perspective as faster.

        # How each perspective views the other is how 
        # that perspective travels through time relative 
        # to the other's perspective.

        # So, if the initial perspective sees the new perspective 
        # as moving slow, really, it's just that the initial 
        # perspective is moving slow relative to the new perspective.

        # On the flip, if the new perspective sees the initial 
        # perspective as moving fast, it's really just that the new 
        # perspective is moving fast relative to the initial perspective.

        #^^^ Same as below, just reworded vvvvv

        # 1. Equal Starting Point: Two observers begin with a shared 
        #     understanding of time and space.

        # 2. Introduction of Gravity: Gravity is added to one observer's 
        #     environment.

        # 3. Perception of Time Dilation:
        #     * The observer without added gravity sees the other 
        #         (in stronger gravity) as moving slower.
        #     * The observer in stronger gravity sees the first observer 
        #         as moving faster.
        
        # 4. Relative Motion: The way one observer perceives the other's 
        #     speed is indicative of their own passage through time relative 
        #     to the other.
        #     * If Observer A sees Observer B (in stronger gravity) as moving 
        #         slower, it's because, from B's perspective, A is actually the 
        #         one moving slower in time relative to B.
        #     * Conversely, if Observer B sees Observer A as moving faster, it's 
        #         because B is moving through time more quickly relative to A.

        print(f"Your perspective (On both observers) **You only can pass through time 1 unit per second")
        print(f"Target point: ({final_pt}, 0)")
        print(f"Current Position: ({curr_pt}, 0)")
        print(f"Complex shortest distance (to final point): {curr_distance}")
        print(f"Real + Imaginary Distance (total complex distance): {i_real_distance}")
        print()
        print(f"Outside Observer Perspective (on inside observer)")
        print(f"Outside point final is {final_pt} (Ends once real reaches this)")
        print(f"Outside Distance Rate (traversing): {real_distance_rate}...")
        print(f"Outside Distance (traveled): {real_distance}...")
        print()
        print(f"Inside observer perspective (on outside observer)")
        print(f"Inside real point final is {format(flip_final_pt, '.5f')} (Ends once real reaches this)")
        print(f"Inside real distance rate (traversing): {format(flip_real_distance_rate, '.5f')}")
        print(f"Inside real distance (traveled): {format(flip_real_distance, '.5f')}")

        # Need to flip, given rate and real traversal, calculate remaining distance and distance traveled
        # Also need to literally give separate perspective. 10 seconds always flows as 10 seconds

        if curr_pt == final_pt:
            print()
            print("You've reached the designated point!")
            print()
            print("Summary: ")
            print(f"In your {i_real_distance} seconds/units of traversal,")
            print(f"The outside observer traveled through: {real_distance} seconds/units")
            print(f"The inside observer traveled through: {flip_real_distance} seconds/units")
            print()
            print(f"In your 1 unit per second 'rate',")
            print(f"The outside observer seemingly travels through {real_distance_rate} units/seconds per 1 of yours")
            print(f"The inside observer seemingly travels through {flip_real_distance_rate} units/seconds per 1 of yours")
            print()

            break

if __name__ == "__main__":
    main()


# Rename variables, change to decimal format, explain how outside observer is basis for you and inside 
    # (Since outside observer is the one you all initially agreed will set as the clock of travel)