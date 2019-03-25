from PurePython import swconstrained as swnumba
from pySeqAlign import swconstrained as swcython
import seaborn as sns
from scipy import stats
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

np.random.seed(0)
sizes = np.arange(8, 40)**2
Ds = [getRandomCSM(s, s) for s in sizes]
i = 0

def compareTimes():
    """
    Show how much raw C saves time wise with a double for loop
    """
    reps = 1000
    # Run numba code once so it compiles
    swnumba(getRandomCSM(10, 10))
    
    # Run cython code
    cytimes = np.zeros(len(sizes))
    nbtimes = np.zeros(len(sizes))
    global i
    for i, s in enumerate(sizes):
        print("Doing %i x %i"%(s, s))
        cytimes[i] = timeit.timeit("swcython(Ds[i].flatten(), Ds[i].shape[0], Ds[i].shape[1])", number=reps, globals=globals())
        nbtimes[i] = timeit.timeit("swnumba(Ds[i])", number=reps, globals=globals())
    sio.savemat("times.mat", {"cytimes":cytimes, "nbtimes":nbtimes})
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(cytimes, nbtimes)
    ax = sns.regplot(x=cytimes, y=nbtimes)
    plt.legend(["y=%.3gx+%.3g (r=%.3g)"%(slope, intercept, r_value)])
    plt.xlabel("Cython")
    plt.ylabel("Numba")
    plt.show()


if __name__ == "__main__":
    compareTimes()
