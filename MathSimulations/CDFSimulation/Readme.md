---

# 📊 CDF Simulation of the Sum of Exponentials

This project simulates the process of constructing the **Cumulative Distribution Function (CDF)** for a random variable \( Z = Y_1 + Y_2 \), where both \( Y_1 \) and \( Y_2 \) are exponentially distributed random variables with a parameter \( \lambda = 1 \). The goal is to estimate the CDF of \( Z \) by simulating 20,000 trials and constructing the relative frequency table for \( F_Z(z) = P(Z \leq z) \) over 100 equally spaced points between 0.0 and 9.9.

## 🔧 Problem Description

- **Objective:** Estimate the CDF of the sum of two independent exponential random variables.
- **Random Variables:**
  - \( Y_1 \sim \text{Exp}(\lambda = 1) \)
  - \( Y_2 \sim \text{Exp}(\lambda = 1) \)
- **Process:** 
  - Sample values for \( Y_1 \) and \( Y_2 \) from the exponential distribution.
  - Compute the sum \( Z = Y_1 + Y_2 \).
  - Use the 20,000 trials to compute relative frequencies \( P(Z \leq z) \) for \( z \in \{0.0, 0.1, 0.2, \ldots, 9.9\} \).
- **Output:** A CDF table similar to the format of the standard normal CDF table, where rows and columns represent intervals in \( Z \).

## 🧠 How It Works

- **Sampling from an Exponential Distribution:** 
  - The exponential distribution can be simulated using a uniform random variable on \( [0, 1) \) via the transformation:
    \[
    Y = -\ln(1 - U)
    \]
    where \( U \) is uniformly distributed on \( [0, 1) \).
  
- **Simulating the Process:**
  - For each trial, sample two independent values from the exponential distribution.
  - Compute the sum \( Z = Y_1 + Y_2 \).
  - Track how many times \( Z \) is less than or equal to a given value of \( z \), for each of the 100 points in the range from 0.0 to 9.9.

## 📊 Results: Sum of Exponentials CDF

The results of the simulation are presented in a tabular format. The table provides the relative frequencies of the event \( Z \leq z \) at each step.

### Example of CDF Table:

|   z  |   0.0  |   0.1  |   0.2  |   0.3  |   0.4  |   0.5  |   0.6  |   0.7  |   0.8  |   0.9  |
|------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0.0  | 0.0000 | 0.0048 | 0.0176 | 0.0378 | 0.0622 | 0.0892 | 0.1226 | 0.1557 | 0.1909 | 0.2271 |
| 1.0  | 0.2632 | 0.3017 | 0.3387 | 0.3723 | 0.4080 | 0.4425 | 0.4754 | 0.5061 | 0.5365 | 0.5663 |
| 2.0  | 0.5954 | 0.6202 | 0.6457 | 0.6703 | 0.6936 | 0.7145 | 0.7353 | 0.7537 | 0.7701 | 0.7866 |
| 3.0  | 0.8005 | 0.8159 | 0.8291 | 0.8427 | 0.8528 | 0.8644 | 0.8752 | 0.8853 | 0.8944 | 0.9023 |
| 4.0  | 0.9101 | 0.9168 | 0.9244 | 0.9304 | 0.9364 | 0.9411 | 0.9461 | 0.9500 | 0.9547 | 0.9582 |
| 5.0  | 0.9618 | 0.9648 | 0.9678 | 0.9705 | 0.9727 | 0.9748 | 0.9770 | 0.9790 | 0.9807 | 0.9821 |
| 6.0  | 0.9837 | 0.9847 | 0.9858 | 0.9864 | 0.9873 | 0.9881 | 0.9892 | 0.9896 | 0.9906 | 0.9913 |
| 7.0  | 0.9921 | 0.9927 | 0.9935 | 0.9941 | 0.9949 | 0.9953 | 0.9957 | 0.9961 | 0.9964 | 0.9967 |
| 8.0  | 0.9969 | 0.9970 | 0.9973 | 0.9974 | 0.9978 | 0.9980 | 0.9983 | 0.9984 | 0.9986 | 0.9987 |
| 9.0  | 0.9987 | 0.9988 | 0.9988 | 0.9990 | 0.9992 | 0.9992 | 0.9992 | 0.9992 | 0.9993 | 0.9993 |

## 🚀 How to Run the Simulation

1. **Install Dependencies:** Make sure you have Python and `numpy` installed.
2. **Run the Script:** Use the provided Python code to generate the CDF table. The code will output the table formatted like the example above.

---
