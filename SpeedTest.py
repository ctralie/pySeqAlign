from PurePython import swconstrained as swnumba
from pySeqAlign import swconstrained as swcython
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import timeit
import sys

def getRandomCSM(N, M):
    D = np.random.rand(N, M)
    D = D < 0.1
    D = np.array(D, dtype='double')
    return D

np.random.seed(1)
D = getRandomCSM(1000, 1000)

def compareTimes():
    """
    Show how much raw C saves time wise with a double for loop
    """
    reps = 1000
    # Run numba code once so it compiles
    swnumba(getRandomCSM(10, 10))
    
    # Run cython code
    cytime = timeit.timeit("swcython(D.flatten(), D.shape[0], D.shape[1])", number=reps, globals=globals())
    cyans = swcython(D.flatten(), D.shape[0], D.shape[1])

    nbtime = timeit.timeit("swnumba(D)", number=reps, globals=globals())
    nbans = swnumba(D)

    print("Cython Time: %.3g, ans=%.3g"%(cytime, cyans))
    print("Numba  Time: %.3g, ans=%.3g"%(nbtime, nbans))

if __name__ == "__main__":
    compareTimes()
