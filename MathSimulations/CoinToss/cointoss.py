import numpy as np
import pandas as pd

# Function to simulate the coin tosses and calculate the relative frequency
def simulate_coin_tosses(n, p, trials):
    bob_more_heads = 0
    
    for _ in range(trials):
        # Bob tosses n+1 coins, Alice tosses n coins
        bob_tosses = np.random.binomial(1, p, n + 1)  # Simulating Bob's coin tosses
        alice_tosses = np.random.binomial(1, p, n)    # Simulating Alice's coin tosses
        
        # Counting the heads
        bob_heads = sum(bob_tosses)
        alice_heads = sum(alice_tosses)
        
        # Check if Bob has more heads than Alice
        if bob_heads > alice_heads:
            bob_more_heads += 1
    
    # Return relative frequency
    return bob_more_heads / trials

# Parameters
n = 300
trials = 1000
probabilities = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# Run the simulation for each probability and store results
results = {p: simulate_coin_tosses(n, p, trials) for p in probabilities}

# Display the results in a table-like format
df = pd.DataFrame(list(results.items()), columns=["p", "Relative Frequency"])
df = df.round(3)

import ace_tools as tools; tools.display_dataframe_to_user(name="Coin Toss Simulation Results", dataframe=df)
