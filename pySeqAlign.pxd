from libcpp.vector cimport vector

cdef extern from "SequenceAlignment.c":
	double swalignimpconstrained(double* S, int N, int M)

cdef extern from "SimilarityFusion.c":
	double snf(float* Ps, float* Ss, int* Js, float* Pts, float* nextPts, float* A, int n_features, int N, int K, int niters, float reg_diag)