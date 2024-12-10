def calculate_power_consumption(report):
    # Number of bits in each binary number
    bit_length = len(report[0])
    
    # Initialize counters for 1s and 0s in each bit position
    ones_count = [0] * bit_length
    total_count = len(report)
    
    # Count the number of 1s in each bit position across all binary numbers
    for binary_number in report:
        for i, bit in enumerate(binary_number):
            if bit == '1':
                ones_count[i] += 1
    
    # Calculate the gamma rate (most common bit in each position)
    gamma_rate_binary = ''.join('1' if ones_count[i] > total_count / 2 else '0' for i in range(bit_length))
    
    # Calculate the epsilon rate (least common bit in each position)
    epsilon_rate_binary = ''.join('0' if ones_count[i] > total_count / 2 else '1' for i in range(bit_length))
    
    # Convert binary to decimal
    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = int(epsilon_rate_binary, 2)
    
    # Calculate power consumption (gamma_rate * epsilon_rate)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption

def get_rating(report, rating_type):
    numbers = report[:]
    bit_length = len(report[0])
    
    for i in range(bit_length):
        # Calculate the count of 1s at the current bit position
        ones_count = sum(1 for num in numbers if num[i] == '1')
        zero_count = len(numbers) - ones_count
        
        if rating_type == "oxygen":
            # Oxygen rating: Keep numbers with most common bit (1 if tied)
            keep_bit = '1' if ones_count >= zero_count else '0'
        elif rating_type == "co2":
            # CO2 rating: Keep numbers with least common bit (0 if tied)
            keep_bit = '0' if zero_count <= ones_count else '1'
        
        # Filter numbers based on the current bit
        numbers = [num for num in numbers if num[i] == keep_bit]
        
        # Stop when only one number remains
        if len(numbers) == 1:
            break
    
    return int(numbers[0], 2)

# # Example usage:
# report = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
# ]

# Read report from input.txt
def read_report_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines, strip newline characters, and return as a list
        return [line.strip() for line in file.readlines()]

report = read_report_from_file('input.txt')

# Calculate life support rating
oxygen_rating = get_rating(report, "oxygen")
co2_rating = get_rating(report, "co2")
life_support_rating = oxygen_rating * co2_rating

print(f"Oxygen Generator Rating: {oxygen_rating}")
print(f"CO2 Scrubber Rating: {co2_rating}")
print(f"Life Support Rating: {life_support_rating}")
