from cmath import inf
from cv2 import threshold
import Auxiliary.s_box as sbox
import os
from random import random,randint,choice
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import Auxiliary.funcs_filtered_outputs_m_3 as m3
import numpy as np
#from keras.models import Sequential
import keras
#from keras.layers import Dense
from tensorflow.keras import Sequential
from tensorflow.keras.layers import  Flatten, Dense

NUM_RULES=2
INPUT_SIZE=8
OUTPUT_SIZE=8

def convert(state):
    converted=np.zeros((NUM_RULES*56),dtype=np.int8)
    for i,j in enumerate(state):
        converted[i*56+j]=1
    return converted

def convert_8(state):
    r=np.where(state==1)[0]
    res=[s%56 for s in r]
    return res

rules_list,rule_names=m3.return_rules()

model = Sequential()
model.add(Dense(56*NUM_RULES, input_shape=(56*NUM_RULES,),batch_size=1,name='inputlayer'))
model.add(Dense(56, activation='relu',name='hiddenlayer'))
model.add(Dense(1, activation='relu',name='outputlayer'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])
# model.summary()
average_reward=0
beta=0.1
epsilon_threshold=0.4
alpha=0.05
gamma=.8
# rules=[m3.rule_178,m3.rule_92,m3.rule_154,m3.rule_18,m3.rule_68,m3.rule_172,m3.rule_222,m3.rule_46]
S=[29, 53]
A_val=randint(0,55)
while(A_val in S):
    A_val=randint(0,55)
A=(randint(0,NUM_RULES-1),A_val)
print(f'Initial State: {[rule_names[s] for s in S]}')
while True:

    print(f"Replacing {rule_names[S[A[0]]]} with {rule_names[A[1]]}...")
    
    S_prime=S.copy()
    S_prime[A[0]]=A[1]
    print(f'Current State: {[rule_names[s] for s in S_prime]}')
    R=sbox.state_crypto_strength(S_prime)
    epsilon = random()
    if epsilon<epsilon_threshold:
        print("Exploring...")
        rand_action=randint(0,55)
        while(rand_action in S_prime):
            rand_action=randint(0,55)
        A_prime=(randint(0,NUM_RULES-1),rand_action)
        taken_state=S_prime.copy()
        taken_state[A_prime[0]]=A_prime[1]
        taken_state=convert(taken_state)
    else:
        print("Exploiting...")
        max_states=[]
        max_actions=[]
        max_value=-inf
        # for i in range(8):
        #     for j in range(56):
        #         if j in S_prime:
        #             continue
        #         next_state=np.zeros((8*56),dtype=np.int8)
        #         for k in S_prime:
        #             if k==S_prime[i]:
        #                 continue
        #             next_state[i*56+k]=1
        #         next_state[i*56+j]=1
        
        for i in range(NUM_RULES):
            current_action=S_prime[i]
            
            for j in range(56):
                if j==current_action:
                    continue
                next_state=convert(S_prime)
                next_state[i*56+current_action]=0
                next_state[i*56+j]=1
                # print('input')
                # print(np.array([np.array(next_state).flatten()]))
                prediction=model.predict(np.array([next_state]))
                # print("prediction")
                # print(prediction)
                if prediction>max_value:
                    max_value=prediction
                    max_states=[next_state]
                    max_actions=[(i,j)]
                elif prediction==max_value:
                    max_states.append(next_state)
                    max_actions.append((i,j))
        action_index=randint(0,len(max_actions)-1)
        taken_state=max_states[action_index]
        A_prime=max_actions[action_index]
    # print("State")
    # print(taken_state)
    Q_s_a=model.predict(np.array([convert(S_prime)]))+sbox.state_crypto_strength(S_prime)
    Q_sprime_aprime=model.predict(np.array([taken_state]))+sbox.state_crypto_strength(convert_8(taken_state))
    target=Q_s_a+alpha*(R-average_reward+gamma*(Q_sprime_aprime)-Q_s_a)
    # print(np.array([target]))
    # print(np.array([convert(S_prime)]))
    model.fit(np.array([convert(S_prime)])
                ,np.array([target]))
    delta=R-average_reward+Q_sprime_aprime-Q_s_a
    average_reward+=beta*delta
    S=S_prime
    A=A_prime
        
                    
                
    
    
