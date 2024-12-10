def calculate_fuel_cost(positions, target_position):
    # Calculate total fuel cost with increasing fuel consumption
    fuel_cost = 0
    for pos in positions:
        # Distance between the current position and the target position
        distance = abs(pos - target_position)
        # The cost for moving this distance is the sum of the first `distance` numbers
        fuel_cost += distance * (distance + 1) // 2  # Sum of first 'distance' numbers
    return fuel_cost

def find_best_alignment(positions):
    # Sort the positions to reduce search space
    positions.sort()
    
    # Find the best position by trying each position in the list
    best_fuel_cost = float('inf')
    best_position = -1
    
    # Try aligning to every position in the list
    for position in range(positions[0], positions[-1] + 1):
        fuel_cost = calculate_fuel_cost(positions, position)
        if fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost
            best_position = position
    
    return best_position, best_fuel_cost

# # Example input
# positions = [16,1,2,0,4,2,7,1,2,14]

# Read positions from input.txt
def read_positions_from_file(file_path):
    with open(file_path, 'r') as file:
        # Assuming the positions are on one line and separated by commas
        positions = list(map(int, file.read().strip().split(',')))
    return positions

# Example usage
file_path = 'input.txt'  # path to your input.txt file
positions = read_positions_from_file(file_path)

# Finding the best alignment
best_position, best_fuel_cost = find_best_alignment(positions)

print(f"The best position is {best_position} with a fuel cost of {best_fuel_cost}.")
