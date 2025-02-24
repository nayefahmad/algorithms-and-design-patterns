"""
Demonstrating speedup in sampling from a Markov matrix. Instead of using a dataframe,
we use a dictionary (O(1) lookup), and we use np.searchsorted (O(nlogn) lookup).
"""


import time

import numpy as np
import pandas as pd

# Create a large transition probability DataFrame for benchmarking
n_states = 10000
n_transitions_per_state = 10

np.random.seed(42)
state_A = np.repeat(np.arange(n_states), n_transitions_per_state)
state_B = np.random.choice(np.arange(n_states), size=n_states * n_transitions_per_state)
transition_prob = np.random.rand(n_states * n_transitions_per_state)
transition_prob /= transition_prob.sum()  # global normalization so all sum to 1.0

df = pd.DataFrame(
    {"state A": state_A, "state B": state_B, "transition_prob": transition_prob}
)

# local normalization so sum is 1.0 for given starting point
df["transition_prob"] = df.groupby("state A")["transition_prob"].transform(
    lambda x: x / x.sum()
)


# Precompute cumulative probabilities for the dictionary-based approach
cumulative_dict = {}
for state, group in df.groupby("state A"):
    cumulative_dict[state] = {
        "state B": group["state B"].values,
        "cumulative_prob": group["transition_prob"].cumsum().values,
    }


# Benchmark df.sample approach
def sample_df_sample(current_state, steps):
    current_state = int(current_state)
    sequence = [current_state]
    for _ in range(steps):
        sub_df = df[df["state A"] == current_state]
        next_state = sub_df.sample(n=1, weights="transition_prob")["state B"].values[0]
        sequence.append(next_state)
        current_state = next_state
    return sequence


# Benchmark dictionary + np.searchsorted approach
def sample_dict_np(current_state, steps):
    current_state = int(current_state)
    sequence = [current_state]
    for _ in range(steps):
        states = cumulative_dict[current_state]["state B"]
        cumulative_probs = cumulative_dict[current_state]["cumulative_prob"]
        random_val = np.random.rand() * cumulative_probs[-1]
        next_state = states[np.searchsorted(cumulative_probs, random_val)]
        sequence.append(next_state)
        current_state = next_state
    return sequence


# Run benchmarks
steps = 100

# Time df.sample approach
start = time.time()
df_sample_sequence = sample_df_sample(0, steps)
df_sample_time = time.time() - start

# Time dictionary + np.searchsorted approach
start = time.time()
dict_np_sequence = sample_dict_np(0, steps)
dict_np_time = time.time() - start

print((df_sample_time, dict_np_time, df_sample_sequence[:10], dict_np_sequence[:10]))
print(df_sample_time / dict_np_time)
print("done")
