import PurePython as SA
import pySeqAlign as SAC
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import time
import sys

def compareTimes():
    """
    Show how much raw C saves time wise with a double for loop
    """
    np.random.seed(1)
    D = np.random.rand(1000, 1000)
    D = D < 0.1
    D = np.array(D, dtype='double')

    start = time.time()
    ans = SAC.swconstrained(D.flatten(), D.shape[0], D.shape[1])
    end = time.time()
    print("Time elapsed C: %g seconds, ans = %g"%(end-start, ans))

    start = time.time()
    ans = SA.swconstrained(D)[0]
    end = time.time()
    print("Time elapsed raw python: %g seconds, ans = %g"%(end - start, ans))

if __name__ == "__main__":
    compareTimes()
