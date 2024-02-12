import numpy as np
from scipy.stats import poisson


# function to find the steady-state distribution using linear algebra.
def limitingdtmc(transitionMtx):
    n = transitionMtx.shape[0]
    A = np.eye(n) - transitionMtx
    A[:, 0] = 1
    b = np.zeros((1, n))
    b[0, 0] = 1
    return np.linalg.solve(A.transpose(), b.transpose())


# consider the case where demand is Poisson
demandRate = 0.5  # average demand per unit time
trunc = 10  # number of states to truncate
states = np.arange(0, trunc + 1)
demandDist = poisson.pmf(states, demandRate)
print("The demand distribution is approximated by ", demandDist)
print(sum(demandDist))  # the demand distribution does not exactly add up to 1!!
demandDist[trunc] = demandDist[trunc] + (1 - sum(demandDist)) # correct the demand distribution
print(sum(demandDist))

P = np.vstack((demandDist, demandDist))
for i in range(2, trunc + 1):
    newrow = np.concatenate((np.zeros(i - 1), demandDist[0:trunc - (i - 2)]))
    newrow[trunc] = newrow[trunc] + (1 - sum(newrow))
    P = np.vstack((P, newrow))

print(P)
print(P.sum(axis=1))

limitingDist = limitingdtmc(P)
print("The steady-state distribution of inventory is ", limitingDist)
print(limitingDist.sum())
expInventory = np.dot(np.arange(0, trunc + 1), limitingDist)
print("The expected inventory is ", expInventory)

# The theoretical result obtained using generating functions
theoryExpInventory = demandRate * (1 + demandRate / (2 * (1 - demandRate)))
print(theoryExpInventory)
