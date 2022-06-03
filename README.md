# RL-based-S-boxes
This is the code for the paper 'Exploring Lightweight S-boxes using Cellular Automata and Reinforcement Learning' 

## Code
The code is written in Python 3 and uses the following packages
1. `numpy`
2. `tensorflow`
3. `os`
4. `keras`
5. `cmath`
6. `random`

To run the code, open the root folder and run the following command `python3 RL.py`
To run the code with different number of semi-bent functions, make the following changes:
- Change `NUM_RULES` in `RL.py`
- Change `NUM_RULES` in `Auxiliary/s_box.py`
- Change initital state variable `S` in `RL.py`

## Folder Structure
- RL.py : The main driver code which runs the Reinforcement Learning algorithm and generates the outputs. The algorithm currently explores 50 new states in each run and then terminates. This values can be changed by changing the `MAX_STATES` value in the code.
- Luca Codes : These are the [codes written by Luca et. al](https://github.com/rymoah/ca-boolfun-construction) for the contruction of the semi-bent functions.
- Auxiliary : The folder contains helper codes used by `RL.py`
  - filtered_outputs_m_3 : List of balanced semi-bent functions of neighbourhood size 3. It is a text file
  - funcs_filtered_outputs_m_3 : Python3 implemented functions for the semi-bent functions in the above listed file.
  - outputs_m_3 : List of all semi-bent functions created from neighbourhood size 2 (balanced and unbalanced).
  - parse_to_python : Python parser code that converts the text list of semi-bent functions to a python implemented functions list
  - s_box.py : This file consists of all the code related to the s-box implementation. 
