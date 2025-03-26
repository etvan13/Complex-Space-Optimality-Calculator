import math
import matplotlib.pyplot as plt

# -------------------------------
# Common helper functions
# -------------------------------
def calculate_distance(x, target):
    """Compute absolute distance between current position and target."""
    return abs(target - x)

def calculate_curvature_rate(real_distance, target_pos, curr_distance):
    """
    Compute curvature rate based on the difference between target and current real distance.
    The denominator includes the current spatial distance from target plus one.
    """
    return (target_pos - real_distance) / (curr_distance + 1)

# -------------------------------
# Euler Mode Functions (Continuous)
# -------------------------------
def calculate_complex_step(rate):
    """Calculate the Euler-based complex step from the given rate."""
    theta = math.acos(rate) if -1 <= rate <= 1 else 0
    return complex(rate, math.sin(theta))

def euler_mode():
    """
    Euler-based (continuous) mode with two operational modes:
    1. Traversal mode: explicit discrete stepping (forward/backward steps).
    2. Rate mode: directly input fluent curvature rates per step.
    """
    try:
        final_dist_input = float(input("Enter final distance (e.g., 10): "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    target_pos = final_dist_input
    real_distance = 0.0
    total_complex_distance = 0.0
    complex_path = []  # Store Euler-based complex steps
    previous_rate = 1.0

    mode_choice = input("Enter 'traverse' for discrete traversal steps or 'rate' for direct rate inputs: ").strip().lower()

    if mode_choice == 'rate':
        print("\nEntering RATE MODE: Input measured curvature rates at each step.")
        while real_distance < target_pos:
            try:
                rate_input = float(input("Enter observed curvature rate (<= current or initial 1.0): "))
            except ValueError:
                print("Invalid input. Enter a numerical rate between -1 and 1.\n")
                continue

            if not 0 < rate_input <= previous_rate:
                print("Rate must be at max current or less than it.\n")
                continue
            if rate_input > previous_rate:
                print(f"Rate must be <= previous rate ({previous_rate:.4f}).\n")
                continue

            step = calculate_complex_step(rate_input)
            complex_path.append(step)
            real_distance += rate_input
            total_complex_distance += 1
            previous_rate = rate_input

            print(f"Accumulated Real Distance: {real_distance:.4f}, Current Complex Step: {step:.4f}")

            if real_distance >= target_pos:
                print("Target real distance reached or surpassed.\n")
                break

    elif mode_choice == 'traverse':
        print("\nEntering TRAVERSAL MODE: Discrete forward/backward stepping.")
        current_pos = 0.0
        positions = [current_pos]

        while real_distance < target_pos:
            try:
                move_input = int(input("Enter movement (negative=backward, positive=forward, 0=exit): "))
            except ValueError:
                print("Invalid input. Enter integer steps.\n")
                continue

            if move_input == 0:
                print("Traversal exited by user.\n")
                break

            direction = 1 if move_input > 0 else -1
            steps = abs(move_input)

            for _ in range(steps):
                current_pos += direction
                total_complex_distance += 1
                curr_distance = calculate_distance(current_pos, target_pos)
                rate = (target_pos - real_distance) / (curr_distance + 1)
                step = calculate_complex_step(rate)
                complex_path.append(step)
                real_distance += rate
                positions.append(current_pos)

                print(f"Position: {current_pos:.4f}, Real Distance: {real_distance:.4f}, Current Rate: {rate:.4f}")

                if real_distance >= target_pos:
                    print("Target real distance reached or surpassed.\n")
                    break

    else:
        print("Invalid mode selected.\n")
        return

    # Summarize final results
    tau_total = sum(complex_path)
    magnitude = abs(tau_total)

    print(f"\nFinal Accumulated Real Distance: {real_distance:.4f}")
    print(f"Total Complex Distance: {total_complex_distance:.4f}")
    print(f"Total Euler Complex Path: {tau_total.real:.4f} + {tau_total.imag:.4f}i")
    print(f"Magnitude of Euler Path: {magnitude:.4f}")

    # Plot the Euler-based complex path
    cumulative = 0 + 0j
    real_parts, imag_parts = [], []
    for step in complex_path:
        cumulative += step
        real_parts.append(cumulative.real)
        imag_parts.append(cumulative.imag)

    plt.figure()
    plt.plot(real_parts, imag_parts, marker='o', linestyle='-', color='blue')
    plt.xlabel("Real Component")
    plt.ylabel("Imaginary Component")
    plt.title("Euler-based Complex Path")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()


# -------------------------------
# Discrete Mode Functions
# -------------------------------
def auto_reach_rate_discrete(current_pos, target_pos, real_distance, total_complex_distance, desired_rate):
    """
    Automatically backtracks (using discrete steps) until the curvature rate falls below the desired threshold.
    """
    direction = -1  # backward step
    while True:
        next_pos = current_pos + direction
        next_complex_distance = total_complex_distance + 1
        next_distance = calculate_distance(next_pos, target_pos)
        next_rate = calculate_curvature_rate(real_distance, target_pos, next_distance)
        if next_rate < desired_rate:
            break
        current_pos = next_pos
        total_complex_distance = next_complex_distance
        real_distance += next_rate
    return current_pos, real_distance, total_complex_distance, next_rate

def discrete_mode():
    """
    Discrete mode uses the original stepping method.
    The user can manually enter forward/backward steps, or use 'auto' to backtrack until a desired rate is achieved.
    This mode outputs only the real magnitude.
    """
    while True:
        try:
            final_dist_input = float(input("Enter final distance (e.g., 10): "))
            break
        except ValueError:
            print("Please enter a valid number.\n")

    current_pos = 0.0
    target_pos = final_dist_input
    real_distance = 0.0
    total_complex_distance = 0.0

    print(f"\nStarting at: ({current_pos}, 0)")
    print(f"Target point: ({target_pos}, 0)\n")

    while True:
        move_input = input("Enter movement amount (negative=backward, positive=forward, 'auto'=auto backtrack, 0=exit): ").strip().lower()

        if move_input == 'auto':
            try:
                desired_rate = float(input("Enter desired curvature rate (e.g., 0.86): "))
            except ValueError:
                print("Invalid curvature rate entered.\n")
                continue

            old_pos = current_pos
            old_real_distance = real_distance
            old_total_complex = total_complex_distance

            current_pos, real_distance, total_complex_distance, final_rate = auto_reach_rate_discrete(
                current_pos, target_pos, real_distance, total_complex_distance, desired_rate)

            print(f"\nAUTO BACKTRACKING COMPLETE")
            print(f"Position changed from {old_pos:.4f} to {current_pos:.4f}")
            print(f"Real Distance changed from {old_real_distance:.4f} to {real_distance:.4f}")
            print(f"Total Complex Distance changed from {old_total_complex:.4f} to {total_complex_distance:.4f}")
            print(f"Final Curvature Rate achieved: {final_rate:.6f}\n")
            continue

        try:
            movement = int(move_input)
        except ValueError:
            print("Invalid input. Enter an integer value or 'auto'.\n")
            continue

        if movement == 0:
            print("Exiting the simulation.")
            break

        direction = 1 if movement > 0 else -1
        step_count = abs(movement)

        old_pos = current_pos
        old_real_distance = real_distance
        old_total_complex = total_complex_distance

        for _ in range(step_count):
            current_pos += direction
            total_complex_distance += 1
            curr_distance = calculate_distance(current_pos, target_pos)
            real_distance_rate = calculate_curvature_rate(real_distance, target_pos, curr_distance)
            real_distance += real_distance_rate
            if real_distance >= target_pos:
                break

        print(f"Movement block complete: {movement} steps")
        print(f"Position changed from {old_pos:.4f} to {current_pos:.4f}")
        print(f"Real Distance changed from {old_real_distance:.4f} to {real_distance:.4f}")
        print(f"Total Complex Distance changed from {old_total_complex:.4f} to {total_complex_distance:.4f}")
        print(f"Current Curvature Rate (last calc): {real_distance_rate:.6f}\n")

        if real_distance >= target_pos:
            print("You've reached or surpassed the target real distance!")
            print(f"\nFinal Accumulated Real Distance: {real_distance:.4f}")
            print(f"Total Complex Distance Magnitude: {total_complex_distance:.4f}")
            break


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("Welcome to the Imaginary Curvature Mapper!")
    mode = input("Choose mode ('discrete' for discrete stepping, 'euler' for Euler-based continuous): ").strip().lower()
    if mode == 'euler':
        euler_mode()
    else:
        discrete_mode()

if __name__ == "__main__":
    main()