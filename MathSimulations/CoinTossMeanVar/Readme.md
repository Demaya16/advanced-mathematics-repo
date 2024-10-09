
---

# 🎲 Coin Toss Simulation Project

This project simulates a random process involving two coins. The goal is to compute the **mean** and **variance** of the number of heads obtained after a random number of flips using simulation methods. The process follows this structure:

1. **Coin 1** is flipped repeatedly until the first head appears. The number of flips, denoted by \( N \), follows a **Geometric distribution** with parameter \( p \), the probability of heads for Coin 1.
2. After obtaining \( N \) flips from Coin 1, we flip **Coin 2** exactly \( N \) times. Each flip has a probability \( q \) of landing heads. The total number of heads in these \( N \) flips is denoted by \( Y \).
3. The process is repeated for different combinations of \( p \) and \( q \), and we compute the experimental **mean** and **variance** of \( Y \).

## 🧠 Problem Description

The goal is to simulate the following process:
- **Coin 1** has a probability \( p \) of landing heads. Flip it until the first head appears. Let \( N \) be the number of flips.
- **Coin 2** has a probability \( q \) of landing heads. Flip it exactly \( N \) times and count how many heads you get.
  
### Key Properties:
- \( N \) is geometrically distributed with parameter \( p \).
- The number of heads from \( N \) flips of Coin 2, \( Y \), is the sum of \( N \) independent **Bernoulli trials** with parameter \( q \).

### Objective:
We want to estimate the **mean** \( E[Y] \) and **variance** \( Var(Y) \) for different values of \( p \) and \( q \) by performing 10,000 trials of this experiment.

## 🔧 Methodology

- **Simulation:** For each combination of \( p \) and \( q \) in the range \{0.1, 0.2, ..., 0.9\}, perform 10,000 trials:
  - Flip Coin 1 until the first head.
  - Flip Coin 2 for the number of flips \( N \) and count the number of heads.
- **Results:** For each combination, calculate the **mean** and **variance** of the number of heads from the Coin 2 flips.

### Parameters
- \( p \) and \( q \) represent the probability of heads for Coin 1 and Coin 2, respectively.
- The simulation runs for values of \( p \) and \( q \) from 0.1 to 0.9 in increments of 0.1.

### Tables:
The results are presented in two tables:
- **Mean Table**: Shows the average number of heads for each combination of \( p \) and \( q \).
- **Variance Table**: Shows the variance of the number of heads for each combination of \( p \) and \( q \).

## 📊 Results

### Mean Table

|  q  | 0.1    | 0.2    | 0.3    | 0.4    | 0.5    | 0.6    | 0.7    | 0.8    | 0.9    |
|-----|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0.1 | 0.9875 | 2.0254 | 2.9935 | 4.0188 | 4.9560 | 5.9829 | 6.9413 | 8.0763 | 9.1051 |
| 0.2 | 0.4893 | 1.0316 | 1.5287 | 2.0412 | 2.4712 | 2.9990 | 3.4531 | 4.0259 | 4.4661 |
| 0.3 | 0.3399 | 0.6727 | 0.9780 | 1.3227 | 1.6885 | 2.0122 | 2.3646 | 2.6611 | 3.0183 |
| 0.4 | 0.2524 | 0.4950 | 0.7433 | 0.9979 | 1.2329 | 1.4951 | 1.7323 | 2.0077 | 2.2451 |
| 0.5 | 0.1979 | 0.3963 | 0.5847 | 0.8147 | 0.9943 | 1.1859 | 1.3924 | 1.6049 | 1.7858 |
| 0.6 | 0.1695 | 0.3308 | 0.5034 | 0.6750 | 0.8328 | 1.0086 | 1.1586 | 1.3278 | 1.4919 |
| 0.7 | 0.1406 | 0.2837 | 0.4308 | 0.5653 | 0.7117 | 0.8563 | 1.0056 | 1.1418 | 1.2922 |
| 0.8 | 0.1259 | 0.2502 | 0.3679 | 0.5001 | 0.6262 | 0.7373 | 0.8810 | 0.9999 | 1.1188 |
| 0.9 | 0.1151 | 0.2257 | 0.3375 | 0.4486 | 0.5600 | 0.6618 | 0.7727 | 0.8897 | 1.0068 |

### Variance Table

|  q  | 0.1       | 0.2      | 0.3      | 0.4      | 0.5      | 0.6      | 0.7      | 0.8      | 0.9      |
|-----|-----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 0.1 | 1.7171    | 5.5074   | 10.3213  | 16.7978  | 24.6279  | 34.7654  | 46.8029  | 61.1647  | 79.1867  |
| 0.2 | 0.6597    | 1.6694   | 2.9652   | 4.7453   | 5.9052   | 8.2620   | 10.6204  | 14.0074  | 16.7757  |
| 0.3 | 0.3906    | 0.8402   | 1.3787   | 2.0728   | 2.8775   | 3.6277   | 4.6913   | 5.3362   | 6.9180   |
| 0.4 | 0.2701    | 0.5418   | 0.8772   | 1.2249   | 1.5185   | 1.9672   | 2.3100   | 2.7886   | 3.2108   |
| 0.5 | 0.1977    | 0.3906   | 0.5976   | 0.8080   | 1.0287   | 1.1491   | 1.4092   | 1.6378   | 1.7799   |
| 0.6 | 0.1644    | 0.3076   | 0.4566   | 0.5746   | 0.6888   | 0.7915   | 0.8772   | 0.9789   | 1.0121   |
| 0.7 | 0.1316    | 0.2482   | 0.3610   | 0.4211   | 0.5090   | 0.5665   | 0.6008   | 0.6153   | 0.6300   |
| 0.8 | 0.1160    | 0.2102   | 0.2872   | 0.3594   | 0.3871   | 0.4101   | 0.4188   | 0.3955   | 0.3663   |
| 0.9 | 0.1041    | 0.1846   | 0.2434   | 0.2852   | 0.3136   | 0.3164   | 0.2946   | 0.2533   | 0.2099   |

## 🚀 How to Run the Simulation

To run the simulation and regenerate the tables:

1. **Install Dependencies:** Make sure you have Python and `numpy` installed.
2. **Run the Script:** Use the provided Python script to perform the simulation and compute the mean and variance for different \( p \) and \(
