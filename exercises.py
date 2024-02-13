import numpy as np

# EXERCISES
# 1. Consider the ergodic Markov chain with transition matrix
P = np.array([[0.4, 0.3, 0.2, 0.1],
              [0.5, 0.4, 0.1, 0.0],
              [0.6, 0.2, 0.1, 0.0],
              [0.7, 0.3, 0.0, 0.0]])
# Find the steady-state distribution using linear algebra.

# 2. Argue that the Markov chain with the transition matrix
P = np.array([[0.1, 0.0, 0.9, 0.0],
              [0.0, 0.3, 0.0, 0.7],
              [0.9, 0.0, 0.1, 0.0],
              [0.0, 0.8, 0.0, 0.2]])
# is not ergodic. Hint: check the n-step transition matrix for several values of n
# Can you still solve pi = pi * P? Why or why not? If so, what is the meaning?

# 3. Argue that the Markov chain with the transition matrix
P = np.array([[0.0, 0.3, 0.0, 0.7],
              [0.1, 0.0, 0.9, 0.0],
              [0.0, 0.8, 0.0, 0.2],
              [0.9, 0.0, 0.1, 0.0]])
# is not ergodic. Hint: check the n-step transition matrix for several values of n
# Can you still solve pi = pi * P? Why or why not? If so, what is the meaning?


