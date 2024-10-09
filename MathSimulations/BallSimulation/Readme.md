
---

# 🎯 Urn Experiment Simulation

This project simulates the urn experiment described in the exercise from *Probability and Random Processes* by Grimmett and Stirzaker. The experiment demonstrates that the probability of the last ball discarded being azure or carmine is equal (1/2), regardless of the initial number of azure and carmine balls.

## 📖 Overview

An urn contains `a` azure balls and `c` carmine balls, where `a > 0` and `c > 0`. Balls are randomly selected from the urn and discarded until a selected ball has a color different from its predecessor. The process continues until only one ball remains, which is the last ball discarded.

The goal of this project is to **experimentally verify** that the probability the last ball is azure is equal to the probability that it is carmine, regardless of the initial values of `a` and `c`.

### 🔍 Problem Statement

The problem is as follows:
- You have an urn with `a` azure balls and `c` carmine balls.
- Balls are randomly selected and discarded until the color of the selected ball changes. This ball is then replaced in the urn, and the process continues.
- The experiment ends when only one ball is left.
  
**Claim:** The probability of the last ball being azure or carmine is equally likely (i.e., 1/2) and is independent of the initial numbers of `a` and `c`.

### 🎯 Objective

The project simulates this process for different values of `a` (10, 20, 30, 40, 50) while keeping the total number of balls constant (`a + c = 100`). For each value of `a`, the experiment is repeated 2000 times to calculate the **relative frequency** of the last ball being azure.

### 📊 Results Table Format

After running the simulation for different values of `a` and `c`, a table is generated showing the relative frequency of the last ball being azure:

```
#azure    #carmine  proportion ending in azure
----------------------------------------------
10        90        0.5035
20        80        0.4955
30        70        0.4990
40        60        0.4970
50        50        0.5025
```

### 🛠️ How It Works

The process simulates randomly discarding balls, with the following steps:
1. Start with `a` azure balls and `c` carmine balls in an urn.
2. Randomly discard balls until a ball with a different color than the previous one is selected.
3. Continue this process until one ball remains.
4. Repeat the experiment for different values of `a` and `c`, and compute the frequency of the last ball being azure over 2000 trials.

---

## 🧑‍💻 How to Run the Simulation

1. **Install Python**:
   Ensure that you have Python installed on your machine. You can download it from [Python's official website](https://www.python.org/).

2. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/demaya16/construction-engineering-repo.git
   ```

3. **Navigate to the Project Directory**:
   Navigate to the directory where the project is located:
   ```bash
   cd urn-experiment
   ```

4. **Run the Simulation**:
   Execute the `urn_simulation.py` file to start the experiment:
   ```bash
   python urn_simulation.py
   ```

5. **View Results**:
   The program will display the table with the relative frequency of the last ball being azure for each value of `a`.

---

## 💻 Code Example

```python
def simulate_process(a, c):
    # Create the urn with 'a' azure balls and 'c' carmine balls
    urn = ['azure'] * a + ['carmine'] * c
    
    # Continue selecting balls until only one ball remains
    while len(urn) > 1:
        first_ball = urn.pop(random.randint(0, len(urn) - 1))
        while True:
            second_ball = random.choice(urn)
            if second_ball != first_ball:
                urn.append(second_ball)
                break
    
    return urn[0]
```

---

## 🛠 Tools and Technologies

- **Python**: The experiment is implemented in Python, a versatile and widely-used programming language for simulations and data processing.

---

## 📈 Expected Output

The output will be a table that displays the relative frequency of the last ball being azure for different values of `a` (10, 20, 30, 40, 50). This verifies that the probability of the last ball being azure remains close to 0.5, regardless of the starting number of azure and carmine balls.

---

## 🔮 Conclusion

This simulation experimentally demonstrates that the last ball discarded is equally likely to be azure or carmine, regardless of the initial distribution of azure and carmine balls in the urn. This probability converges to 1/2 as the number of trials increases.

Feel free to explore the code, adjust the parameters, and run additional experiments to further validate the claim!

---

