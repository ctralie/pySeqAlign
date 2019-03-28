cimport numpy as np
cimport pySeqAlign as seq
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def swconstrained(np.ndarray[double,ndim=1,mode="c"] SParam not None, int N, int M):

	res = seq.swalignimpconstrained(&SParam[0], N, M)

	return res


@cython.boundscheck(False)
@cython.wraparound(False)
def snfcython(np.ndarray[float,ndim=1,mode="c"] Ps not None, np.ndarray[float,ndim=1,mode="c"] Ss not None, np.ndarray[int,ndim=1,mode="c"] Js not None, np.ndarray[float,ndim=1,mode="c"] Pts not None,
np.ndarray[float,ndim=1,mode="c"] nextPts not None, np.ndarray[float,ndim=1,mode="c"] A not None, int n_features, int N, int K, int niters, float reg_diag):

	seq.snf(&Ps[0], &Ss[0], &Js[0], &Pts[0], &nextPts[0], &A[0], n_features, N, K, niters, reg_diag)