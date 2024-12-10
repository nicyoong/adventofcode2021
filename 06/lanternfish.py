def simulate_lanternfish(fish_timers, days):
    # Initialize a list where index represents the timer value of each fish (0-8)
    fish_counts = [0] * 9
    
    # Populate the initial fish counts based on the provided list of timers
    for timer in fish_timers:
        fish_counts[timer] += 1
    
    # Simulate the fish population for the given number of days
    for _ in range(days):
        # Fish that create new fish today (those with timer 0)
        new_fish = fish_counts[0]
        
        # Shift the fish timers down by 1 (everyone gets one day closer to their next cycle)
        for i in range(8):
            fish_counts[i] = fish_counts[i + 1]
        
        # Reset the fish with timer 0 to timer 6 and add new fish with timer 8
        fish_counts[6] += new_fish
        fish_counts[8] = new_fish
    
    # The total number of fish is the sum of all fish in all timer states
    return sum(fish_counts)

# # Example input
# fish_timers = [3, 4, 3, 1, 2]

# Read fish timers from 'input.txt'
with open('input.txt', 'r') as file:
    # Read the single line from the file and convert it to a list of integers
    fish_timers = list(map(int, file.read().strip().split(',')))

# Simulate for 80 days
result = simulate_lanternfish(fish_timers, 80)
print("Total lanternfish after 80 days:", result)
