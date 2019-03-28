from libcpp.vector cimport vector

cdef extern from "SequenceAlignment.c":
	double swalignimpconstrained(double* S, int N, int M)
