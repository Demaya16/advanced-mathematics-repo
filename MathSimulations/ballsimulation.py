import random

# Function to simulate the process and return the color of the last ball discarded
def simulate_process(a, c):
    # Create the urn with 'a' azure balls and 'c' carmine balls
    urn = ['azure'] * a + ['carmine'] * c
    
    # Continue selecting balls until only one ball remains
    while len(urn) > 1:
        # Draw the first ball
        first_ball = urn.pop(random.randint(0, len(urn) - 1))
        
        # Draw balls until one different from the first is selected
        while True:
            second_ball = random.choice(urn)
            if second_ball != first_ball:
                urn.append(second_ball)  # Replace the last ball of different color
                break
    
    # Return the color of the last ball
    return urn[0]

# Function to run the experiment for a given 'a' and 'c' (2000 trials)
def run_experiment(a, c, trials=2000):
    azure_count = 0
    for _ in range(trials):
        if simulate_process(a, c) == 'azure':
            azure_count += 1
    
    # Calculate the relative frequency of the last ball being azure
    return azure_count / trials

# Main function to simulate for different values of a (10, 20, 30, 40, 50)
def main():
    trials = 2000
    total_balls = 100
    results = []
    
    # Run the simulation for different values of 'a' and corresponding 'c'
    for a in [10, 20, 30, 40, 50]:
        c = total_balls - a
        frequency_azure = run_experiment(a, c, trials)
        results.append((a, c, frequency_azure))
    
    # Print the results in a formatted table
    print(f"{'#azure':<10} {'#carmine':<10} {'proportion ending in azure':<25}")
    print("-" * 50)
    for a, c, freq in results:
        print(f"{a:<10} {c:<10} {freq:<25.4f}")

if __name__ == "__main__":
    main()
