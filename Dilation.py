import math
from decimal import Decimal, getcontext

# Set the desired precision to 50 significant digits
getcontext().prec = 50
getcontext().Emin = -999999 #Set low to avoid scientific notation

def show_intro(level=0):
    # Base case for the recursive function
    if level == 0:
        intro_text ='''

Welcome to the Time Dilation Simulator!
          
        Discover the intriguing effects of gravity on time through the eyes of three observers:
            1. You: Observe from a neutral point, where time flows consistently at 1 unit per second.
            2. Observer A: Moves towards gravity, experiencing time more slowly.
            3. Observer B: Moves away from gravity, where time speeds up.
        
        How It Works:
            * Move "Left": Adds gravity for Observer A, slowing their time.
            * Move "Right": Reduces gravity for Observer B, speeding up their time.
            
        Your Mission: Watch as Observer A aims for a target. Your actions influence their journey, 
            showcasing how gravity bends the fabric of time.

            Ready to see time warp before your eyes?
        
    Press 'enter' to begin, or type "expand" and press 'enter' to read further!\n'''
        
    elif level == 1:
        intro_text = '''
The Triangle of Observers:

        Imagine a triangle where each point represents one of the three observers. Initially, 
        all are at the same point—forming a perfect equilateral triangle. You're at the base, 
        Observer A is at the top left, and Observer B at the top right. Initially, all exist 
        in a state free from any relativistic effects of time dilation.

        Movement and Time Dilation:
            * Right Movement (Time at Rest): Selecting a 'right' move keeps the triangle's structure 
                intact but lets time tick uniformly for all observers. This is a pause, allowing 
                every observer to experience time at a consistent rate within their frame.
            * Left Movement (Spatial Expansion): Opting for a 'left' move makes the triangle expand. 
                Observer A heads towards a weaker gravitational field, while Observer B moves towards 
                a stronger one. This expansion is spatial—each observer drifts 1 unit per second from 
                your viewpoint, ignoring the dilation initially, but introduces the dilation effects 
                observed in the simulation (an equilateral triangle that distorts).

        Visualizing the Triangle:
            With each 'left' move, the triangle's expansion visually depicts the varying perceptions 
            of time due to gravity's relativistic impacts:

            * The side leading to Observer A, moving into stronger gravity, elongates slower, mirroring 
                their stretched time.
            * The side reaching towards Observer B, heading into lesser gravity, lengthens faster, 
                signifying their quicker passage of time from your perspective.
        
        The Observer's Perspective:
            From your position at the triangle's base, you watch the two vertices separate with each 
            'left' move. This divergence in their temporal experiences is symbolized by the triangle's 
            expansion. It acts as a metaphor for spacetime stretching under gravity's sway, influencing 
            each observer's time flow.
            
    Press 'enter' to begin, or type "expand" and press 'enter' to read further!\n'''
                

    elif level == 2:
        intro_text = '''
Understanding Physical Space and Spacetime
    
    In our journey through the relativistic effects of gravity on time, we've visualized the movement 
    of our observers as an expanding equilateral triangle in physical space. We must consider two 
    perspectives on the situation at hand. On where the triangle exists in physical space, and another 
    where the triangle exists in spacetime 'iSpace'.
    
    The Equilateral Triangle in Physical Space:
        * Unchanged Proportions: In physical space, given each frame of reference, each observer would 
            'see' the triangle as equilateral uniformly expanding with each 'left' movement. This 
            represents each observer moving symmetrically away from the starting point, maintaining equal 
            spatial relations with one another. This is true given their frame of observation.
        * Constant Spatial Movement: Despite the gravitational effects, the physical space between the 
            observers expands at a constant rate, perceived as 1 unit per second from your perspective. 
            This uniform expansion symbolizes the physical distance they cover, irrespective of the 
            relativistic time effects.
    
    The Triangle in Spacetime (iSpace): A Unified Perspective
        As the observers expand from one another, they perceive an expanding equilateral triangle 
        respective to their own gravitational context. However, each observer percieving their own clock 
        as 'normal' would visualize the other two observers as having changing rates. This divergence in 
        time perception affects how each observer views the expansion of the triangle.
        
        Spacetime: A Perspective Binding Fabric
            * Composite Frames: Spacetime serves as a canvas that merges these individual perceptions 
                into a singular, unified frame. This frame draws an equilateral triangle that accomodates 
                all frames into one, but by doing so, this triangle 'bends' inwards and outwards to 
                accomodate for each perspective.
            * Percieved Geometry: Within this unified spacetime framework, what appears as an equilateral 
                triangle in each observer's frame transforms when viewed from the comprehensive spacetime 
                perspective. The triangle's sides, representing the paths between observers, no longer 
                conform strictly to equilateral geometry due to the curvature induced by differing time 
                flows.
                    - Think of it like a strange shape. When you look at it, it looks 'normal', but when 
                        you rotate it, it's completely different than how it originally looked. It's 
                        still the same shape, just differs based on how you look at it!

            Bridging Individual Realities:
                * Relativity of Straight Lines: Ever heard "The shortest distance between two points is 
                    not always a straight line"?, well this is exactly why! Just as a straight line in 
                    spacetime can curve, so too can our equilateral triangle warp, accomodating the 
                    realtive nature of time and space as experienced by each observer.
                * The Illusion of Equilaterality: While each observer perceives an equilateral triangle 
                    expanding within their frame, the incorporation of these perspectives into the 
                    singular spacetime grid reveals a more complex shape, illustrating the relativistic 
                    interplay between space and time. 

    Press 'enter' to begin, or type "expand" and press 'enter' to read further!\n'''
    
    elif level == 3:
        intro_text = '''
Spacetime Through the Lens of Complex Numbers

    In mathematics, complex numbers offer a way to extend the real number line by introducing an 
    imaginary component, denoted by 'i'. This concept mirrors the fabric of spacetime, where the "real" 
    part corresponds to our observable dimensions and the "imaginary" part represents the hidden 
    dimensions or effects, like time dilation, that we can't directly perceive.

    Spacetime and Complex Numbers:
    * Real Component: In the context of spacetime, the real component can be likened to the observable 
        spatial dimensions within an observer's frame. This is the part of spacetime that we can 
        directly measure and perceive.
    * Imaginary Component: The imaginary part of spacetime, akin to the imaginary unit 'i' in complex 
        numbers, symbolizes the aspects of spacetime that elude direct perception, such as the 
        curvature induced by gravity. This component accounts for the "bending" of spacetime, allowing 
        for phenomena like time dilation.

    The Scaling Quantity in Spacetime:
        * Defining Curvature: Just as the magnitude of the imaginary part in a complex number defines 
            the extent of deviation from the real axis, the "scaling quantity" in spacetime represents 
            the degree to which time and space are curved due to gravitational effects. This curvature 
            allows spacetime to "stretch" or "compress," accommodating more events or distances within 
            a given segment of the real (observable) part.
        * Storing Values Along the 'Invisible' Line: The imaginary component in complex numbers allows 
            us to represent values and operations that don't fit on the traditional real number line. 
            Similarly, the "imaginary" aspect of spacetime enables us to conceptualize how an observer 
            can traverse or experience more space or time than what appears constrained by the real 
            dimensions, like fitting 20 units of experience within a 5-unit span of observable space.

    Mathematical Insights into Relativity:
        This mathematical analogy sheds light on the intricacies of spacetime and relativity, offering 
        a way to grasp the otherwise abstract concepts of time dilation and spacetime curvature. It 
        highlights how spacetime accommodates the vast range of relativistic phenomena within a coherent 
        framework, much like how complex numbers encompass both real and imaginary components to form a 
        complete picture.
        
        Press 'enter' to begin.\n'''
    
    else:
        return  # Exit the function and continue with the rest of the program

    # Show the intro text for the current level
    user_input = input(f"{intro_text}\n> ")

    # If user types 'expand', recursively call the function with the next level
    if user_input.lower() == 'expand':
        show_intro(level + 1)
    else:
        return  # User typed something other than 'expand', so return and continue the program

# Function to calculate the distance to B
def calculate_distance(x, final_pt):
    return abs(final_pt - x)

def main():
    show_intro()

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

        print("--- Your Spacetime Perspective ---")
        print(f"From your vantage point, observing spacetime unfold at a constant rate of 1 temporal unit per movement:")
        print(f"Convergence Point: ({final_pt}, 0)")
        print(f"Your Current Coordinate: ({curr_pt}, 0)")
        print(f"Dimensional Distance to Convergence: {curr_distance} units")
        print(f"Spacetime Passage: {i_real_distance} temporal units")
        print()

        print("--- Observer A's Gravitational Journey ---")
        print(f"Observer A's convergence with stronger gravity alters their temporal flow:")
        print(f"Target Convergence: {final_pt} units")
        print(f"Time Dilation Rate: {real_distance_rate:.10f} (slower time perception)")
        print(f"Spacetime Traversed: {real_distance:.20f} units")
        print()

        print("--- Observer B's Escape from Gravity ---")
        print(f"Observer B's journey away from gravity affects their temporal experience:")
        print(f"Extended Convergence Point: {flip_final_pt:.5f} units")
        print(f"Time Contraction Rate: {flip_real_distance_rate:.5f} (accelerated time perception)")
        print(f"Spacetime Traversed: {flip_real_distance:.5f} units")

        if curr_pt == final_pt:
            print("\nYou've reached the convergence point in spacetime!")
            print("\n--- Journey Recap ---")
            print(f"Throughout your journey spanning {i_real_distance} seconds:")
            print(f"Observer A (approaching gravity) experienced a passage of {real_distance:.5f} seconds/units.")
            print(f"Observer B (receding from gravity) navigated through {flip_real_distance:.5f} seconds/units.")
            print("\n--- Relative Time Flow ---")
            print(f"From your vantage point in spacetime, each temporal unit (second/space unit) for you corresponded to:")
            print(f"{real_distance_rate:.5f} seconds for Observer A, illustrating the dilation of time near stronger gravity.")
            print(f"{flip_real_distance_rate:.5f} seconds for Observer B, reflecting the contraction of time as gravity lessens.")
            print("\nThis encapsulation showcases the relativity of time and space as influenced by gravity,")
            print("demonstrating how each observer's traversal through spacetime varies from their unique perspective.")


            break

if __name__ == "__main__":
    main()
