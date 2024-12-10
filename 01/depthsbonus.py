def count_sliding_window_increases(depths, window_size=3):
    """
    Count the number of times the sum of a sliding window increases 
    compared to the previous window.

    :param depths: List of integers representing depths
    :param window_size: Size of the sliding window (default is 3)
    :return: Integer count of increases
    """
    count = 0
    for i in range(len(depths) - window_size):
        # Calculate the sum of the current and next sliding window
        current_window_sum = sum(depths[i:i + window_size])
        next_window_sum = sum(depths[i + 1:i + 1 + window_size])
        if next_window_sum > current_window_sum:
            count += 1
    return count

# Read depths from input.txt
def read_depths_from_file(filename):
    """
    Read depths from a file where each line is a number.
    
    :param filename: Path to the input file
    :return: List of integers representing depths
    """
    with open(filename, 'r') as file:
        depths = [int(line.strip()) for line in file]
    return depths

# Load depths from the file
input_file = 'input.txt'
depths = read_depths_from_file(input_file)

# Call the function and print the result
result = count_sliding_window_increases(depths)
print(f"Number of sliding window increases: {result}")
