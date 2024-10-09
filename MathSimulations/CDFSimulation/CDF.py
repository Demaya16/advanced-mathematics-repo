import numpy as np

# Number of trials
trials = 20000

# Generate 100 equally spaced points from 0.0 to 9.9
z_values = np.arange(0.0, 10.0, 0.1)

# Store the results for each z value
cdf_results = np.zeros_like(z_values)

# Define a function to sample from an exponential distribution with lambda = 1
def sample_exponential():
    u = np.random.uniform(0, 1)
    return -np.log(1 - u)

# Simulate the experiment
for _ in range(trials):
    # Sample Y1 and Y2 from the exponential distribution
    Y1 = sample_exponential()
    Y2 = sample_exponential()
    
    # Compute Z = Y1 + Y2
    Z = Y1 + Y2
    
    # Update the CDF for each z_value
    for i, z in enumerate(z_values):
        if Z <= z:
            cdf_results[i] += 1

# Convert to relative frequencies
cdf_results = cdf_results / trials

# Format the results into the required table structure
cdf_table = cdf_results.reshape(10, 10)

import pandas as pd
cdf_df = pd.DataFrame(cdf_table, columns=[f"{i/10:.1f}" for i in range(10)], index=[f"{i}.0" for i in range(10)])
cdf_df
