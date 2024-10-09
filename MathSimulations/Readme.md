
---

# 🧮 **Advanced Mathematics and Simulations Repository** 🧮

Welcome to the **Advanced Mathematics and Simulations Repository**, a comprehensive collection of mathematical simulations, random process experiments, and computational projects that showcase advanced probability, statistics, and random process theory. Each project is structured to explore and simulate complex mathematical principles, ranging from basic probability distributions to more advanced topics such as random variables, coin tosses, and exponential distributions.

---

## 📂 **Repository Overview**

This repository contains multiple sub-projects, each focusing on different areas of mathematical simulations and probability experiments. The projects are organized under the **MathSimulations** folder and other subfolders with related topics.

### **1. Coin Toss Simulation (Bob vs Alice)**

- **Objective**: Simulate a coin-toss experiment to determine the probability that Bob tosses more heads than Alice using \( n \)-coin trials.
- **Problem**: Given a set of independent coin tosses by Bob and Alice, calculate the relative frequency of Bob obtaining more heads than Alice over multiple trials.
- **Results**: Demonstrates the statistical approach to calculating relative frequency and how the probability changes with different coin probabilities.

### **2. Urn Selection Process**

- **Objective**: Simulate a random process involving two types of balls (azure and carmine) selected randomly from an urn until the last ball is discarded.
- **Problem**: Show experimentally that the last ball discarded has a 50% chance of being azure or carmine, independent of the initial configuration.
- **Results**: Provides relative frequencies and insights into why the probability distribution of the last ball is independent of the initial number of azure or carmine balls.

### **3. Lottery Game Simulation (Joe Lucky)**

- **Objective**: Simulate Joe Lucky’s weekly lottery play and determine the joint probability mass functions (PMF) for the number of weeks Joe plays and the number of weeks he wins.
- **Problem**: Use simulation to estimate the joint PMF, conditional PMFs, and marginal PMFs for various lottery win and play scenarios.
- **Results**: Demonstrates statistical relationships between the number of weeks played, won, and the conditional probabilities.

### **4. Two Coin Simulation**

- **Objective**: Simulate flipping two different coins, one with a probability \( p \) of heads and the other with a probability \( q \), and analyze the mean and variance of the second sequence of coin flips.
- **Problem**: Compute the mean and variance of a random process where the number of flips of the second coin depends on the outcome of the first.
- **Results**: Provides tables of mean and variance estimates for different combinations of \( p \) and \( q \), showcasing the relationship between parameters.

### **5. Exponential Sum Simulation**

- **Objective**: Construct the cumulative distribution function (CDF) of the sum of two exponential random variables.
- **Problem**: Use Monte Carlo simulations to estimate the CDF of \( Z = Y_1 + Y_2 \), where both \( Y_1 \) and \( Y_2 \) are exponentially distributed.
- **Results**: A comprehensive table of relative frequencies that approximates the CDF of the sum of exponentials, with in-depth results presented for the range \( z \in [0, 9.9] \).

---

## 🧑‍🏫 **Folder Structure**

The repository is divided into several folders, each containing code and reports for their respective simulations and projects. 

### **advanced-mathematics-repo/MathSimulations/**

- This folder contains various mathematical simulations, including:
  - **Mathematical Theorem Simulations**: Code and results for simulating real-world scenarios using mathematical theorems, including probability theory and statistical analysis.
  - **Probability Experiments**: Experimental simulations of random processes, coin tosses, and urn selection problems.
  - **Game Theory and Strategy**: Projects focused on simulating strategic decision-making scenarios using probability and game theory.

### **Subfolders**

- **CoinTossSimulations/**: Code and experiments related to the Bob vs. Alice coin toss simulation.
- **UrnProcessSimulations/**: The urn selection process simulations, showing statistical properties of random ball selection.
- **LotteryGameSimulations/**: Simulates Joe Lucky’s lottery game and explores joint and conditional PMFs.
- **ExponentialSimulations/**: CDF simulations for the sum of two exponential random variables.

---

## 🚀 **How to Use the Repository**

1. **Clone the Repository**: Clone the repository to your local machine using `git clone`.
   ```bash
   git clone https://github.com/demaya16/advanced-mathematics-repo.git
   ```
2. **Navigate to Specific Projects**: Each project is stored in its own subfolder with all relevant files, code, and data. Simply navigate to the project you want to run.
   ```bash
   cd advanced-mathematics-repo/MathSimulations/ExponentialSimulations
   ```
3. **Run the Code**: All simulations are written in Python and can be executed with standard Python commands. Most projects require basic libraries like `numpy` and `matplotlib`.
   ```bash
   python simulation.py
   ```

---

## 📈 **Results & Reports**

- Each project folder includes a detailed report that discusses the results, along with tables and graphs generated during the simulation process.
- **Reports** are provided in PDF format under the corresponding project folder.

---

## 🛠️ **Requirements**

- **Python 3.x**: Make sure you have Python installed.
- **Dependencies**: The required dependencies can be installed using `pip`:
  ```bash
  pip install numpy matplotlib
  ```

---

This repository is a collection of advanced mathematical simulations and random process experiments. Each project provides valuable insights into probability theory and its applications, making this repository a great resource for anyone looking to explore advanced mathematics and simulations.

---


