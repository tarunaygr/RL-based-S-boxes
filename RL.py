from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras import Sequential
import keras
import numpy as np
import Auxiliary.funcs_filtered_outputs_m_3 as m3
from cmath import inf
import Auxiliary.s_box as sbox
import os
from random import random, randint
from statistics import mean,pstdev
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

NUM_RULES = 2
INPUT_SIZE = 8
OUTPUT_SIZE = 8
MAX_STATES=50

#   This function converts the integer list representation to a version that can be given as input to the ANN
#   Parameters:
#     state: The list of function index in the list rules_list. Values range from 0-55.
    
def convert(state):
    converted = np.zeros((NUM_RULES*56), dtype=np.int8)
    for i, j in enumerate(state):
        converted[i*56+j] = 1
    return converted

#This function does the inverse of convert(). It converts the ANN input to a form easily understandable.
#   Parameters:
#     state: Input to the ANN.
def convert_8(state):
    r = np.where(state == 1)[0]
    res = [s % 56 for s in r]
    return res


rules_list, rule_names = m3.return_rules()

#Creating the function approximator (ANN)

if NUM_RULES==3:
    try:
        model=keras.models.load_model('ann3')
        print('Importing Model..')
    except:
        model = Sequential()
        model.add(Dense(56*NUM_RULES, input_shape=(56*NUM_RULES,),
                batch_size=1, name='inputlayer'))
        model.add(Dense(56, activation='relu', name='hiddenlayer'))
        model.add(Dense(1, activation='relu', name='outputlayer'))
        model.compile(loss='mse', optimizer='adam', metrics=['mae'])
elif NUM_RULES==2:
    try:
        model=keras.models.load_model('ann2')
        print('Importing Model..')
    except:
        model = Sequential()
        model.add(Dense(56*NUM_RULES, input_shape=(56*NUM_RULES,),
                batch_size=1, name='inputlayer'))
        model.add(Dense(56, activation='relu', name='hiddenlayer'))
        model.add(Dense(1, activation='relu', name='outputlayer'))
        model.compile(loss='mse', optimizer='adam', metrics=['mae'])


#Reinforcement Learning

average_reward = 0
beta = 0.1
epsilon_threshold = 0.4
alpha = 0.05
gamma = .8
best_strength = -inf
best_DU = -inf
best_NL = -inf
best_states = []
visited_states = []
strengths=[]
DUs=[]
NLs=[]
worst_strength = inf
worst_DU = inf
worst_NL = inf
S = [4, 20] #These values indicate the function index in the list rules_list. Values range from 0-55.
A_val = randint(0, 55)
A = (randint(0, NUM_RULES-1), A_val)
print(f'Initial State: {[rule_names[s] for s in S]}')
try:
    while (len(visited_states)<MAX_STATES):

        print(f"Replacing {rule_names[S[A[0]]]} with {rule_names[A[1]]}...")

        S_prime = S.copy()
        S_prime[A[0]] = A[1]
        print(f'Current State: {[rule_names[s] for s in S_prime]}')
        R, DU, NL = sbox.state_crypto_strength(S_prime, True)
        if S_prime not in visited_states:
            visited_states.append(S_prime)
            strengths.append(R)
            DUs.append(DU)
            NLs.append(NL)
        if(R < worst_strength):
            worst_strength = R
            worst_DU = DU
            worst_NL = NL
        if(R > best_strength):
            best_strength = R
            best_DU = DU
            best_NL = NL
            best_states = [[rule_names[s] for s in S_prime]]
        elif (R == best_strength and ([rule_names[s] for s in S_prime] not in best_states)):
            best_states.append([rule_names[s] for s in S_prime])
        epsilon = random()
        if epsilon < epsilon_threshold:
            print("Exploring...")
            rand_action = randint(0, 55)
            while(rand_action in S_prime):
                rand_action = randint(0, 55)
            A_prime = (randint(0, NUM_RULES-1), rand_action)
            taken_state = S_prime.copy()
            taken_state[A_prime[0]] = A_prime[1]
            taken_state = convert(taken_state)
        else:
            print("Exploiting...")
            max_states = []
            max_actions = []
            max_value = -inf
            for i in range(NUM_RULES):
                current_action = S_prime[i]

                for j in range(56):
                    if j == current_action:
                        continue
                    next_state = convert(S_prime)
                    next_state[i*56+current_action] = 0
                    next_state[i*56+j] = 1
                    prediction = model.predict(np.array([next_state]))
                    if prediction > max_value:
                        max_value = prediction
                        max_states = [next_state]
                        max_actions = [(i, j)]
                    elif prediction == max_value:
                        max_states.append(next_state)
                        max_actions.append((i, j))
            action_index = randint(0, len(max_actions)-1)
            taken_state = max_states[action_index]
            A_prime = max_actions[action_index]
        Q_s_a = model.predict(np.array([convert(S_prime)]))+R
        Q_sprime_aprime = model.predict(np.array(
            [taken_state]))+sbox.state_crypto_strength(convert_8(taken_state), False)[0]
        target = Q_s_a+alpha*(R-average_reward+gamma*(Q_sprime_aprime)-Q_s_a)
        model.fit(np.array([convert(S_prime)]), np.array([target]))
        delta = R-average_reward+Q_sprime_aprime-Q_s_a
        average_reward += beta*delta
        S = S_prime
        A = A_prime
        
    if NUM_RULES==2:
        model.save('ann2')
    elif NUM_RULES==3:
        model.save('ann3')
        
        
    print("Exiting the RL...\n")
    print("FINAL REPORT:")
    print(f'Number of States Visited: {len(visited_states)}')
    print(f"Best Strength: {round(best_strength,2)}")
    print(f"Worst Strength: {round(worst_strength,2)}")
    print(f'Best DU: {best_DU} Best NL: {best_NL}')
    print(f'Worst DU: {worst_DU} Worst NL: {worst_NL}')
    print(f'Average Strength of visited States: {round(mean(strengths),2)}')
    print(f'Standard Deviation of strength: {round(pstdev(strengths),2)}')
    print(f'Number of states with best strengths: {len(best_states)}')
    print('Best States:')
    print(best_states)
except KeyboardInterrupt:
    #Save The ANN for future
    if NUM_RULES==2:
        model.save('ann2')
    elif NUM_RULES==3:
        model.save('ann3')
        
        
    print("Exiting the RL...\n")
    print("FINAL REPORT:")
    print(f'Number of States Visited: {len(visited_states)}')
    print(f"Best Strength: {round(best_strength,2)}")
    print(f"Worst Strength: {round(worst_strength,2)}")
    print(f'Best DU: {best_DU} Best NL: {best_NL}')
    print(f'Worst DU: {worst_DU} Worst NL: {worst_NL}')
    print(f'Average Strength of visited States: {round(mean(strengths),2)}')
    print(f'Standard Deviation of strength: {round(pstdev(strengths),2)}')
    print(f'Number of states with best strengths: {len(best_states)}')
    print('Best States:')
    print(best_states)
