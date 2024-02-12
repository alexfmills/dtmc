import numpy as np

failProb = 0.1  # p
repairProb = 0.7  # q

P = np.array([[1 - repairProb, repairProb],
              [failProb, 1 - failProb]])  # Probability transition matrix

print("The transition matrix is ", P)
print("The sum of rows is ", P.sum(axis=1), " (should be 1)")

theoryLimitingProb = repairProb / (repairProb + failProb)
print("The steady-state up-time as derived on the whiteboard is ", theoryLimitingProb)

print("The machine is working now. What is the probability it will be working two days from now?")
P2 = np.linalg.matrix_power(P, 2)
print(P2)  # two-step transition matrix
print(P2[1, :])  # two-step state probability distribution starting in state 1
print(P2[1, 1])  # two-step probability of being in state 1 given starting in state 1
ans = P2[1, 1]
print("The machine is working now. In two days, the probability it will be working is ", ans)

print("What is the steady-state up-time of the machine?")
# quick-and-dirty approach: envisioning "steady-state" as just "after many days"
P10 = np.linalg.matrix_power(P, 10)
print("The 10-step transition matrix is ", P10)
# using linear algebra
# we would like to solve pi = pi * P; with sum(pi)=1
# re-write as pi * (I - P) = 0; with sum(pi) = 1
# Write A = (I - P) with the first row replaced by ones; b = 0 with the first column replaced by ones
A = np.eye(2) - P
A[:, 0] = 1
b = np.zeros((1, 2))
b[0, 0] = 1
limitingProb = np.linalg.solve(A.transpose(), b.transpose())
print(limitingProb)
print("The uptime is ", limitingProb[1])

