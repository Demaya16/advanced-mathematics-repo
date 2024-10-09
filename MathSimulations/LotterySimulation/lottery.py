import numpy as np

# Parameters
n = 7  # number of weeks
p = 0.6  # probability Joe plays the lottery on any week
q = 0.7  # probability Joe wins the lottery if he plays
num_trials = 100000  # number of trials

# Initialize frequency table for joint PMF (x, y), where 0 ≤ y ≤ x ≤ n
joint_freq = np.zeros((n + 1, n + 1))

# Simulation
for _ in range(num_trials):
    x = 0  # number of weeks Joe played
    y = 0  # number of weeks Joe won
    for week in range(n):
        if np.random.rand() < p:  # Joe plays
            x += 1
            if np.random.rand() < q:  # Joe wins
                y += 1
    joint_freq[x, y] += 1

# Convert frequency table to joint PMF
joint_pmf = joint_freq / num_trials

# Calculate marginal PMFs
p_x = np.sum(joint_pmf, axis=1)  # p_X(x)
p_y = np.sum(joint_pmf, axis=0)  # p_Y(y)

# Calculate conditional PMF p(X|Y)
cond_pmf_x_given_y = np.zeros((n + 1, n + 1))
for y in range(n + 1):
    if p_y[y] > 0:
        cond_pmf_x_given_y[:, y] = joint_pmf[:, y] / p_y[y]

# Calculate conditional PMF p(Y|X)
cond_pmf_y_given_x = np.zeros((n + 1, n + 1))
for x in range(n + 1):
    if p_x[x] > 0:
        cond_pmf_y_given_x[x, :] = joint_pmf[x, :] / p_x[x]

# Function to print the table
def print_table(pmf, title):
    print(f"\n{title}")
    print("    " + "   ".join([f" {y} " for y in range(n + 1)]))
    print(" " + "-" * 70)
    for x in range(n + 1):
        row = " | ".join([f"{pmf[x, y]:.4f}" for y in range(n + 1)])
        print(f"{x} | {row}")

# Output the tables
print_table(joint_pmf, "Joint PMF of X and Y")
print_table(cond_pmf_x_given_y, "Conditional PMF of X given Y")
print_table(cond_pmf_y_given_x, "Conditional PMF of Y given X")
