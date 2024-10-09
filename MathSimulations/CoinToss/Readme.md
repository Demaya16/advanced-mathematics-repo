# 🧠 **Simulating Coin Toss Probability Experiment** 🧠

This project simulates the coin toss experiment w/ Alice & Bob. The objective is to explore the probability of Bob obtaining more heads than Alice when they both toss different sets of coins under varying probabilities of heads. This simulation investigates how this probability might depend on the probability of a head, denoted as \( p \), and provides insights into the strength of this dependency.

---

## 📊 **Project Overview**

In this simulation project, we examine the probability that **Bob** gets more heads than **Alice** when they toss an uneven number of coins. Specifically:

1. **Bob** tosses \( n+1 \) coins.
2. **Alice** tosses \( n \) coins.
3. We simulate the experiment using independent coin tosses for both, where the probability of a head for each coin is \( p = \frac{1}{2} \).
4. The goal is to compute the relative frequency of Bob tossing more heads than Alice after performing **1000 trials** with \( n = 300 \) and check if it is close to \( \frac{1}{2} \).
5. The experiment is repeated with varying values of \( p \) (i.e., the probability of heads) to explore how \( p \) affects the outcome.

---

## 💻 **Steps and Simulated Process**

1. **Initial Setup:**
   - **Bob** tosses \( n+1 \) coins and **Alice** tosses \( n \) coins where \( n = 300 \).
   - The simulation is conducted over **1000 trials**.

2. **Key Metric:** 
   - We compute the **relative frequency** of Bob tossing more heads than Alice.
   - The relative frequency formula:
     \[
     \text{Relative Frequency} = \frac{\text{Number of trials where Bob tossed more heads}}{\text{Total number of trials}}
     \]
   
3. **Varying Probability \( p \):**
   - In addition to the base case where \( p = \frac{1}{2} \), we modify \( p \) to different values from the set \( \{0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8\} \).
   - We observe how the relative frequency of Bob tossing more heads than Alice changes with different values of \( p \).

---

## 🔍 **Experiment Structure**

### **Objective 1: Initial Simulation with \( p = \frac{1}{2} \)**

We first simulate the experiment with \( p = \frac{1}{2} \), where each coin has an equal chance of landing heads or tails. The expected probability of Bob getting more heads than Alice should be close to \( \frac{1}{2} \) after performing 1000 trials.

### **Objective 2: Experiment with Different Probabilities \( p \)**

Next, we extend the experiment by running the simulation with different values of \( p \) from the set \( \{0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8\} \). For each value of \( p \), we conduct 1000 trials and compute the relative frequency that Bob gets more heads than Alice. This helps us explore how much the probability of Bob getting more heads is influenced by \( p \).

---

## 📋 **Results Table**

| \( p \)   | Relative Frequency of Bob Tossing More Heads |
|-----------|----------------------------------------------|
| 0.2       | 0.xxx                                        |
| 0.3       | 0.xxx                                        |
| 0.4       | 0.xxx                                        |
| 0.5       | 0.xxx                                        |
| 0.6       | 0.xxx                                        |
| 0.7       | 0.xxx                                        |
| 0.8       | 0.xxx                                        |

*Note: The actual values will be generated after running the simulation.*

---

## 📈 **Analysis and Conjecture**

Based on the simulation results for various values of \( p \), we aim to form a conjecture regarding the relationship between the **probability of heads \( p \)** and the **probability of Bob getting more heads than Alice**:

- **Strong Dependence:** If the relative frequency changes significantly across different values of \( p \).
- **Weak Dependence:** If the relative frequency shows only minor variations across different values of \( p \).
- **No Dependence:** If the relative frequency remains close to \( \frac{1}{2} \) regardless of \( p \).

This analysis will help identify whether the probability of Bob tossing more heads than Alice is influenced by the underlying probability of a head or remains consistent across different scenarios.

---

## ⚙️ **Technologies & Tools Used**

- **Python**: Used to simulate the coin tosses and compute the results.
- **NumPy**: Utilized for efficient numerical simulations.
- **Matplotlib**: Optional tool for visualizing the results of the experiment in graphical form.

---

## 📂 **How to Run the Simulation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/demaya16/coin-toss-simulation
   cd coin-toss-simulation
   ```

2. **Run the Python Simulation:**
   Make sure you have **Python 3.x** installed. Run the simulation with the following command:
   ```bash
   python coin_toss_simulation.py
   ```

3. **Modify \( p \) Values:**
   You can modify the \( p \) values by adjusting the list of probabilities inside the Python script.

4. **View Results:**
   The program will display the relative frequency of Bob tossing more heads for each value of \( p \) in the console.

---

## 📝 **Conclusion**

This project successfully simulates the experiment of Bob and Alice tossing different sets of coins, exploring the probability of Bob getting more heads. By varying the probability \( p \), we aim to gain insights into how the probability affects the outcome and whether Bob's advantage remains constant.
