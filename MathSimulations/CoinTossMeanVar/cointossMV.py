import numpy as np

# Number of trials
trials = 10000

# Values for p and q
p_values = np.arange(0.1, 1.0, 0.1)
q_values = np.arange(0.1, 1.0, 0.1)

# Initialize tables for mean and variance
mean_table = np.zeros((9, 9))
variance_table = np.zeros((9, 9))

# Simulation function
def simulate_experiment(p, q, trials):
    heads_counts = []
    for _ in range(trials):
        # Step 1: Flip Coin 1 until the first head appears (Geometric distribution)
        N = np.random.geometric(p)

        # Step 2: Perform N flips of Coin 2 and count the number of heads
        flips_coin2 = np.random.binomial(1, q, N)
        Y = np.sum(flips_coin2)  # Number of heads in Coin 2 flips

        heads_counts.append(Y)

    # Compute mean and variance for the trials
    return np.mean(heads_counts), np.var(heads_counts)

# Perform simulation for each combination of p and q
for i, p in enumerate(p_values):
    for j, q in enumerate(q_values):
        mean, variance = simulate_experiment(p, q, trials)
        mean_table[i, j] = mean
        variance_table[i, j] = variance

# Display the results in tabular form
import pandas as pd

mean_df = pd.DataFrame(mean_table, index=p_values, columns=q_values)
variance_df = pd.DataFrame(variance_table, index=p_values, columns=q_values)

mean_df, variance_df
