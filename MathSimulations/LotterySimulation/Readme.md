
---

# 🎰 Joe Lucky Lottery Simulation

## Project Overview

This project simulates the lottery behavior of Joe Lucky, who plays the lottery independently on any given week with a probability \(p\). Each time he plays, he has a probability \(q\) of winning, also independently of all other weeks. The simulation will explore and compute the **joint PMF**, **conditional PMF of X given Y**, and **conditional PMF of Y given X** based on these parameters.

We run this simulation over a period of \(n\) weeks, where:
- \(X\) represents the number of weeks Joe played the lottery.
- \(Y\) represents the number of weeks Joe won the lottery.

By running the simulation for 100,000 trials, we aim to estimate:
1. **Joint PMF of X and Y**: The probability distribution of both Joe playing and winning the lottery.
2. **Conditional PMF of X given Y**: The probability Joe played the lottery given he won a certain number of times.
3. **Conditional PMF of Y given X**: The probability Joe won the lottery given he played a certain number of times.

## 🎯 Objectives

1. **Simulate Joe's Lottery Activity**: 
   - Each week, Joe plays the lottery with probability \(p\) and wins with probability \(q\) (if he played that week).
   - Repeat this simulation for 100,000 trials.
   
2. **Compute the Joint and Conditional PMFs**:
   - **Joint PMF** \(p_{X,Y}(x,y)\): The probability Joe played \(x\) times and won \(y\) times.
   - **Conditional PMF \(p_{X|Y}(x|y)\)**: The probability Joe played \(x\) times given he won \(y\) times.
   - **Conditional PMF \(p_{Y|X}(y|x)\)**: The probability Joe won \(y\) times given he played \(x\) times.

3. **Present the Results in Tables**:
   - Display the joint and conditional PMFs in well-formatted tables for parameter values \(n = 7\), \(p = 0.6\), and \(q = 0.7\).

## 📊 Results

The simulation will output the following tables:
1. **Joint PMF of X and Y**: Represents the probability distribution of both Joe's plays and wins.
2. **Conditional PMF of X given Y**: Given Joe won \(y\) times, this table shows how many times he played.
3. **Conditional PMF of Y given X**: Given Joe played \(x\) times, this table shows how many times he won.

These tables are crucial to understanding the relationship between Joe's participation in the lottery and his success.

## ⚙️ Simulation Details

- **Number of Weeks (n)**: 7
- **Probability Joe Plays (p)**: 0.6
- **Probability Joe Wins (q)**: 0.7
- **Number of Trials**: 100,000

The process for each trial:
- For each of the 7 weeks, determine if Joe plays the lottery (with probability \(p = 0.6\)).
- If he plays, determine if Joe wins the lottery (with probability \(q = 0.7\)).
- Count how many times Joe played and how many times he won during those 7 weeks.
- Store the frequency of each outcome pair \((x, y)\), where \(x\) is the number of times Joe played and \(y\) is the number of times he won.

## 🧪 How to Run the Simulation

1. **Requirements**: 
   - Python 3.x
   - Numpy library (`pip install numpy`)

2. **Run the Simulation**:
   - Clone or download the repository.
   - Navigate to the folder containing the script.
   - Run the Python script:
     ```bash
     python joe_lucky_lottery_simulation.py
     ```

3. **Outputs**:
   - The simulation will generate the joint and conditional PMFs and print them in a readable table format.

## 🔍 Example Tables

### Joint PMF of X and Y:
```plaintext
   y:   0       1       2       3       4       5       6       7
 x ------------------------------------------------------------------
 0 |  0.0000  0.0000  ...
 1 |  0.0000  0.0000  0.0000
 ...
```

### Conditional PMF of X given Y:
```plaintext
   y:   0       1       2       3       4       5       6       7
 x ------------------------------------------------------------------
 0 |  0.0000  ...
 ...
```

### Conditional PMF of Y given X:
```plaintext
   y:   0       1       2       3       4       5       6       7
 x ------------------------------------------------------------------
 0 |  0.0000
 ...
```

## 📚 Interpretation

The PMF tables provide insights into Joe’s lottery behavior. The conditional PMFs \(p_{X|Y}(x|y)\) and \(p_{Y|X}(y|x)\) offer an understanding of Joe's playing and winning patterns over time.

## 🔧 Tools & Technologies Used

- **Python**: For the implementation of the simulation.
- **Numpy**: Used for handling random number generation and array operations.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For questions or further inquiries, feel free to reach out via [Email](mailto:demaya1601@gmail.com) or visit my [GitHub Profile](https://github.com/demaya16).

---
