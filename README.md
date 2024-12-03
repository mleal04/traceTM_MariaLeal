# Team Name: MariaLeal
## Team Members
- Maria Leal → mleal2

## Overall Project Attempted, with Sub-projects
- **Program 1**: Tracing NTM Behavior

## Overall Success of the Project
The project was completed successfully for the chosen language for the NTM.

## Total Time to Complete
- Approximately 1 day

## Link to GitHub Repository
- [GitHub Repository](https://github.com/mleal04/traceTM_MariaLeal/tree/main)

---

## List of Included Files
### Code Files
- **traceTM_MariaLeal/main/ntmCreateTrace_MariaLeal.py**  
  This file reads the CSV test files, creates the NTM class, and processes the test string, outputting whether it was accepted or rejected by the NTM.

### Test Files
- **traceTM_MariaLeal/main/check_ntm1.csv**
- **traceTM_MariaLeal/main/check_ntm2.csv**
- **traceTM_MariaLeal/main/check_ntm3.csv**
- **traceTM_MariaLeal/main/check_ntm4.csv**
- **traceTM_MariaLeal/main/check_ntm5.csv**  
  These files contain the test case data, including the transitions and string information required to test the NTM.

### Output Files
- **traceTM_MariaLeal/main/output_test_cases.txt**  
  This file contains the output of the program, detailing the name of the machine, the input string, the number of transitions, degree of nondeterminism, and the tracing path taken.

### Plots
- No plots were needed for this project.

---

## Programming Languages Used, and Associated Libraries
- **Python**  
- Libraries: `import csv`

## Key Data Structures
- **Classes** (OOP)
- **Hash tables**
- **Arrays and lists**
- **Strings**

## General Operation of Code
### traceTM_MariaLeal/main/ntmCreateTrace_MariaLeal.py
In this file, the `NTM` class is used to define the components of a nondeterministic Turing machine (NTM), including states, transitions, and the input string. The class reads information from the CSV files to set up the machine and trace the input string through possible transitions. The tracing function explores the nondeterministic paths and prints the sequence of configurations until the machine either accepts or rejects the string.

### traceTM_MariaLeal/main/check_ntm[1,2,3,4,5].csv
These CSV files contain the necessary information to define the NTM:
- Name of the machine
- Starting string for the test case
- Number of states and their names
- Starting, accepting, and rejecting states
- The transitions of the NTM

These files are read by the Python file to define the NTM machine.

### traceTM_MariaLeal/main/output_test_cases.txt
This file contains the program's output, which includes:
- The name of the machine
- The test string
- The number of transitions
- The degree of nondeterminism
- The tracing path taken during execution

---

## Test Cases Used, Why They Were Used, and What They Told About the Code

All test cases are stored in the CSV files. The language in use is `L = ab+a`.

- **Abbba**: This test case explores how the NTM loops through multiple 'b's.
- **Aba**: This minimal test case checks how the NTM handles a simple string with one 'b'.
- **Abbbbbbba**: This test case verifies how the NTM handles a long sequence of 'b's.
- **Aa**: This case checks the NTM's ability to reject strings with no 'b's.
- **Ba**: This case checks how the NTM rejects strings starting with 'b'.

These cases helped verify the correctness of the code by ensuring it works for both accepted and rejected strings, covering basic and complex scenarios.

---

## How You Managed the Code Development
I started by creating my CSV files and then began reading the information into the NTM class. Once the NTM class was functioning, I proceeded to implement the tracing logic.

---

## Detailed Discussion of Results
- **Test Case 1 (abbba)**: The machine accepts the string in 12 transitions, demonstrating its ability to handle multiple 'b's between the 'a's. The nondeterminism is visible as the machine explores different paths.
- **Test Case 2 (aba)**: The machine accepts the string in 6 transitions, showing that even minimal cases are efficiently handled.
- **Test Case 3 (abbbbbbba)**: The machine accepts this longer string in 24 transitions, highlighting how it processes extended sequences of 'b's.
- **Test Case 4 (aa)**: The machine rejects the string after 2 transitions, confirming it correctly handles strings without 'b's.
- **Test Case 5 (ba)**: The machine rejects the string after 1 transition, demonstrating the early identification of invalid input.

Each test case highlights the NTM's handling of different input patterns and nondeterministic transitions.

---

## How the Team Was Organized
I worked by myself.

---

## What You Might Do Differently if You Did the Project Again
I would likely create the NTM class before making the test cases, as I did not think of the structure of the code until after I had started creating the test cases.

---

## Any Additional Material
None.
