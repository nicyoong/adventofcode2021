def count_increases(depths):
    """
    Count the number of times a depth measurement increases 
    from the previous measurement.
    
    :param depths: List of integers representing depths
    :return: Integer count of increases
    """
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
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
result = count_increases(depths)
print(f"Number of increases: {result}")
