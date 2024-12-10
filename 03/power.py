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

# Example usage:
report = read_report_from_file('input.txt')

print(calculate_power_consumption(report))
