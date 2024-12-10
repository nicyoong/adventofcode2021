def count_easy_digits(entries):
    # Define the segment counts for the easy digits
    easy_digit_lengths = {2, 4, 3, 7}  # The segment lengths for digits 1, 4, 7, and 8

    count = 0
    for entry in entries:
        # Split the entry at the '|' symbol
        patterns, output_values = entry.split(" | ")
        
        # Split both parts into their respective words (patterns or output values)
        output_digits = output_values.split()

        # Count how many of the output digits have a segment length in easy_digit_lengths
        for digit in output_digits:
            if len(digit) in easy_digit_lengths:
                count += 1

    return count


# # Sample input
# entries = [
#     "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
#     "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
#     "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
#     "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
#     "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
#     "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
#     "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
#     "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
#     "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
#     "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
# ]

# Function to read the entries from input.txt
def read_entries_from_file(filename):
    with open(filename, 'r') as file:
        entries = file.read().splitlines()
    return entries

# Read the entries from 'input.txt'
entries = read_entries_from_file('C:\\Users\\Streaming\\Git\\adventofcode2021\\08\\input.txt')

# Call the function and print the result
result = count_easy_digits(entries)
print(f"The result is {result}")
